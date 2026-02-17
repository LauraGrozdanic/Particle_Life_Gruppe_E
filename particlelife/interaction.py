"""
interaction.py

Computes interaction forces between particles based on their types.
Uses Numba (@njit) to run faster.

"""

import numpy as np
from numba import njit

# types: 0=Purple, 1=Red, 2=Green, 3=Yellow
INTERACTION_MATRIX = np.array(
    [
        [-0.3, 0.2, -0.1, 0.4],  # Purple reacts to (Purple, Red, Green, Yellow)
        [0.1, -0.3, 0.3, -0.2],  # Red reacts to (Purple, Red, Green, Yellow)
        [-0.4, 0.1, -0.3, 0.2],  # Green reacts to (Purple, Red, Green, Yellow)
        [0.3, -0.4, 0.2, -0.3],  # Yellow reacts to (Purple, Red, Green, Yellow)
    ]
)

"""
Interaction matrix: defines how each particle type reacts
to each other. Positive values attract, negative values repel.
"""

@njit
def compute_forces(x, y, types, matrix, max_distance, interaction_strength):

    """
    Computes the interaction forces between all particles.

    For each particle pair (i, j), a force is calculated based on:

    1. Distance:
       - Only particles that are closer than max_distance interact.
       - Distance normalized as r = distance / max_distance.

    2. Particle types:
       - Interaction matrix defines attraction (positive) or repulsion (negative) between types.
       - Value is scaled by interaction_strength.

    3. Distance zones:
       - r < 0.15  - strong repulsion (avoids overlap)
       - r < 0.6   - attraction (particles move to each other)
       - r >= 0.6  - weak repulsion in long range (prevents large clusters)

    The force that results is added to fx and fy for each particle.

    Parameters:

    x, y: np.ndarray
        Arrays containing the particle positions.
    types: np.ndarray
        Array with the particle type index (0–3).
    matrix: np.ndarray
        Interaction matrix defines attraction/repulsion.
    max_distance: float
        Maximum interaction range.
    interaction_strength: float
        Global scaling factor for all interaction forces.

    Returns:

    fx, fy: np.ndarray
        The total force applied to each particle in x and y.
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

            distance = np.sqrt(dx * dx + dy * dy)

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
