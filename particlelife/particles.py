import numpy as np
# from .interaction import compute_interaction_direction

class Particles:
    """
    The class stores particle positions, velocities and particle types.
    It also provides simple motion update utilities:
    - "diffuse" adds random difussion and applies the current velocity
    - "wrap_arounf" applies periodic boundary conditions
    """

    def __init__ (self, n_points=1000):
        self.n_points = n_points

        # Random start positions around (0, 0), scale=10 -> controls how spread out they are
        self.x = np.random.normal(loc=0.0, scale=10.0, size=n_points)
        self.y = np.random.normal(loc=0.0, scale=10.0, size=n_points)
        
        
        # Start with zero velocity
        self.vx = np.zeros(n_points)
        self.vy = np.zeros(n_points)

       
        self.types = np.repeat(np.arange(4), n_points // 4)
        np.random.shuffle(self.types)
        
        self.colors = np.array([
            [0.0, 1.0, 1.0],  # Typ0:turquoise
            [1.0, 0.0, 0.0],  # Typ1:red
            [0.0, 1.0, 0.0],  # Typ2:green
            [1.0, 1.0, 0.0],  # Typ3:yellow
        ])

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
