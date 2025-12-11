import numpy as np
from .interaction import compute_interaction_direction

class Particles:
    def __init__ (self, n_points=1000):
        self.n_points = n_points
        self.x = np.random.normal(loc=0.0, scale=10.0, size=n_points)
        self.y = np.random.normal(loc=0.0, scale=10.0, size=n_points)
        self.vx = np.zeros(n_points)
        self.vy = np.zeros(n_points)

    def diffuse(self, n_step=0.1):
        self.x += np.random.normal(scale=n_step, size=self.x.shape)
        self.y += np.random.normal(scale=n_step, size=self.y.shape)
        self.x += self.vx
        self.y += self.vy
        return self.x, self.y
