"""
interaction.py

Computes interaction forces between particles based on their types.
Uses Numba (@njit) to run faster.

"""

import numpy as np
from numba import njit

# types: 0=Turq, 1=Red, 2=Green, 3=Yellow
INTERACTION_MATRIX = np.array([
        [-0.3,  0.2, -0.1,  0.4], # Turquoise reacts to (Turq, Red, Green, Yellow)
        [ 0.1, -0.3,  0.3, -0.2], # Red reacts to (Turq, Red, Green, Yellow)
        [-0.4,  0.1, -0.3,  0.2], # Green reacts to (Turq, Red, Green, Yellow)
        [ 0.3, -0.4,  0.2, -0.3], # Yellow reacts to (Turq, Red, Green, Yellow)
])

@njit
def compute_forces(x, y, types, matrix, max_distance, interaction_strength):
    """ 
    Calculate the force (fx, fy) on each particle from all other particles.
    Only particles closer than max_distance interact.
    """
    n = len(x)
    fx = np.zeros(n)
    fy = np.zeros(n)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            dx = x[j] - x[i]
            dy = y[j] - y[i]

            distance = np.sqrt(dx*dx + dy*dy)

            if distance == 0.0 or distance > max_distance:
                continue

            direction_x = dx / distance
            direction_y = dy / distance

            strength = matrix[types[i], types[j]] * interaction_strength
            r = distance / max_distance

            if r < 0.15:
                factor = -1.0
            elif r < 0.6:
                factor = 0.8 * (0.6 - r)
            else:
                factor = -0.02

            force = strength * factor

            fx[i] += direction_x * force
            fy[i] += direction_y * force

    return fx, fy



