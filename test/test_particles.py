import numpy as np
from particlelife.particles import Particles


def test_wrap_around():
    p = Particles(n_points=3)

    # set 3 particles out of bounds
    p.x = np.array([-5.0, -1.0, 15.0])
    p.y = np.array([-10.0, 0.0, 10.0])

    # set left and right border
    xmin, xmax = 0.0, 10.0
    # set upper and lower border
    ymin, ymax = -5.0, 5.0
    
    p.wrap_around(xmin, xmax, ymin, ymax)

    # test if all particles are inside the borders
    assert np.all(p.x >= xmin) and np.all(p.x < xmax)
    assert np.all(p.y >= ymin) and np.all(p.y < ymax)
  

def test_diffuse():
    # Creates 2 particles
    p = Particles(n_points=2)

    # fixed start positions (nothing is random)
    p.x = np.array([0.0, 1.0])
    p.y = np.array([10.0, 20.0])

    # fixed velocities
    p.vx = np.array([1.0, -2.0])
    p.vy = np.array([0.5, 0.0])

    # no random noise, only movement from vx/vy
    x_new, y_new = p.diffuse(n_step=0.0)

    expected_x = np.array([1.0, -1.0])
    expected_y = np.array([10.5, 20.0])

    # check if it matches exactly
    assert (x_new == expected_x).all()
    assert (y_new == expected_y).all()

    
def test_interactions_no_change_when_no_force_and_friction():
    # Create 3 particles
    p = Particles(n_points=3)
    # Set particle types manually (important for small n_points)
    p.types = np.array([0, 1, 2], dtype=np.int64)
    # Set known velocities
    p.vx = np.array([1.0, -2.0, 3.0])
    p.vy = np.array([4.0, -5.0, 6.0])
    # Apply interactions with no force and no friction
    p.apply_interactions(
        max_distance=10,
        interaction_strength=0.0,  
        friction=1.0, )
    # Velocities should stay exactly the same
    assert np.allclose(p.vx, np.array([1.0, -2.0, 3.0]))
    assert np.allclose(p.vy, np.array([4.0, -5.0, 6.0]))


def test_apply_interactions_creates_velocity():
    # Create 2 particles
    p = Particles(n_points=2)
    # Set particle types manually
    p.types = np.array([0, 1], dtype=np.int64)
    # Place particles close to each other
    p.x = np.array([0.0, 1.0])
    p.y = np.array([0.0, 0.0])
    # Start with zero velocity
    p.vx = np.array([0.0, 0.0])
    p.vy = np.array([0.0, 0.0])
    # Apply interactions (forces should act)
    p.apply_interactions(
        max_distance=10,
        interaction_strength=1.0,  
        friction=1.0,              
    )
    # Velocity should change (not remain zero)
    assert not np.allclose(p.vx, 0.0)
