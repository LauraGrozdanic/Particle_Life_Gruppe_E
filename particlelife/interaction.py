# Interaktion zwischen partikeln

import numpy as np

INTERACTION_MATRIX = np.array([
    #        0 (Türkis)  1 (Rot)   2 (Grün)  3 (Gelb)
    [  0.3,  -0.4,       0.5,     -0.2],   # 0 = Türkis
    [ -0.2,   0.3,      -0.4,      0.5],   # 1 = Rot
    [  0.5,  -0.2,       0.3,     -0.4],   # 2 = Grün
    [ -0.4,   0.5,      -0.2,      0.3],   # 3 = Gelb
])

def compute_interaction_direction(pos_i, pos_j, type_i, type_j,
                                  matrix=INTERACTION_MATRIX,
                                  max_distance=50,
                                  interaction_strength=1.0):

    delta = pos_j - pos_i
    distance = np.linalg.norm(delta)

    if distance == 0 or distance > max_distance:
        return np.zeros(2)

    # Richtung normieren
    direction = delta / distance

    # Stärke aus Matrix
    strength = matrix[type_i][type_j] * interaction_strength


    r = distance / max_distance

    if r < 0.1:
        factor = -2.0 * (0.1 - r)        # starke Repulsion
    elif r < 0.4:
        factor = 1.5 * (r - 0.1)         # Attraction
    elif r < 0.7:
        factor = -0.5 * (r - 0.4)        # leichte Repulsion
    else:
        factor = 0.0
     
    return direction * strength * factor




