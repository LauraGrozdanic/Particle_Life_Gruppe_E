import numpy as np
from particlelife.particles import Particles


def test_wrap_around():
    p = Particles(n_points=3)

    # 3 Partikel absichtlich außerhalb setzen
    p.x = np.array([-5.0, -1.0, 15.0])
    p.y = np.array([-10.0, 0.0, 10.0])

    # linke und rechte Grenze setzen
    xmin, xmax = 0.0, 10.0
    # obere und untere Grenze setzen
    ymin, ymax = -5.0, 5.0

    p.wrap_around(xmin, xmax, ymin, ymax)

    # testen ob alle wieder im Bereich sind
    assert np.all(p.x >= xmin) and np.all(p.x < xmax)
    assert np.all(p.y >= ymin) and np.all(p.y < ymax)
  
#=======================second test ====================================================
"""
    If interaction_strength is 0 and friction is 1,
    velocities must stay exactly the same.
"""
def test_interactions_no_change_when_no_force_and_friction():
    p = Particles(n_points=3)

    # Fix types manually for the test
    p.types = np.array([0, 1, 2], dtype=np.int64)

    p.vx = np.array([1.0, -2.0, 3.0])
    p.vy = np.array([4.0, -5.0, 6.0])

    p.apply_interactions(
        max_distance=10,
        interaction_strength=0.0,
        friction=1.0,
    )

    assert np.allclose(p.vx, np.array([1.0, -2.0, 3.0]))
    assert np.allclose(p.vy, np.array([4.0, -5.0, 6.0]))