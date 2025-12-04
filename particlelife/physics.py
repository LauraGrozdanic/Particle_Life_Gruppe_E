import numpy as np

def diffuse(x, y, n_step=0.1):
    x += np.random.normal(scale=n_step, size=x.shape)
    y += np.random.normal(scale=n_step, size=y.shape)
    return x, y