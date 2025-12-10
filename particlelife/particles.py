import numpy as np

class Particles:
    def __init__ (self, n_points=1000):
        self.n_points = n_points
        self.x = np.random.normal(loc=0.0, scale=10.0, size=n_points)
        self.y = np.random.normal(loc=0.0, scale=10.0, size=n_points)


    def diffuse(self, x, y, n_step=0.1):
        self.x += np.random.normal(scale=n_step, size=x.shape)
        self.y += np.random.normal(scale=n_step, size=y.shape)
        return x, y
