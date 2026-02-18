import numpy as np
from .interaction import INTERACTION_MATRIX, compute_forces


class Particles:
    def __init__(self, n_points, friction):
        """
        The class stores particle positions, velocities and particle types.
        It also provides simple motion update utilities:
        - "diffuse" adds random difussion and applies the current velocity
        - "wrap_around" applies periodic boundary conditions
        """
        self.n_points = n_points
        self.friction = friction

        # Random start positions around (0, 0), scale=10 -> controls how spread out they are
        self.x = np.random.normal(loc=0.0, scale=10.0, size=n_points)
        self.y = np.random.normal(loc=0.0, scale=10.0, size=n_points)

        # Start with zero velocity
        self.vx = np.zeros(n_points)
        self.vy = np.zeros(n_points)

        self.types = np.repeat(np.arange(4), n_points // 4)
        np.random.shuffle(self.types)

        self.colors = np.array(
            [
                [0.85, 0.70, 1.00],  # Typ0:purple
                [1.0, 0.0, 0.0],  # Typ1:red
                [0.0, 1.0, 0.0],  # Typ2:green
                [1.0, 1.0, 0.0],  # Typ3:yellow
            ]
        )

    def diffuse(self, n_step=0.1):
        """
        Update positions by diffusion noise (n_step) and velocity.
        Returns the updated (x, y) arrays.
        """

        # Random diffusion (Brownian motion)
        self.x += np.random.normal(scale=n_step, size=self.x.shape)
        self.y += np.random.normal(scale=n_step, size=self.y.shape)

        # Applies current velocity
        self.x += self.vx
        self.y += self.vy
        return self.x, self.y

    def apply_interactions(
        self, max_distance=50, interaction_strength=1.0):
        
        """
        calculation and application of interaction forces between particles. 

        Particles influence each other depending on their type and distance.
        Forces are computed using the interaction matrix and added to
        the particle velocities.

        friction factor is used to slow down the movement and keep
        the simulation stable.

        Parameters:

        max_distance: float
            Maximum distance at which particles affect each other.
        interaction_strength: float
            Controls how strong the interaction forces are.
        friction: float
            Reduces velocity each step to avoid instability. 
        """

        fx, fy = compute_forces(
            self.x,
            self.y,
            self.types,
            INTERACTION_MATRIX,
            max_distance,
            interaction_strength,
        )

        self.vx += 0.01 * fx
        self.vy += 0.01 * fy

        # friction
        self.vx *= self.friction
        self.vy *= self.friction

    def wrap_around(self, xmin, xmax, ymin, ymax):
        """
        Apply periodic boundary conditons.
        If a particle leaves the siumlation bounds on one side, it re-enters on the opposite side.
        This keeps all particles within the square.
        """

        # Size of the area
        width = xmax - xmin
        height = ymax - ymin

        # Keeps x and y inside the valid range using modulo
        self.x = ((self.x - xmin) % width) + xmin
        self.y = ((self.y - ymin) % height) + ymin
