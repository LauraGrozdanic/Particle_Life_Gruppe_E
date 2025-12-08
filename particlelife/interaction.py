# Interaktion zwischen partikeln

import numpy as np

INTERACTION_MATRIX = np.array([
    [ 0.0,  1.0, -1.0,  0.0],  # Typ 0 reagiert so auf 0,1,2,3
    [-1.0,  0.0,  1.0,  0.0],  # Typ 1
    [ 1.0, -1.0,  0.0,  0.0],  # Typ 2
    [ 0.0,  0.0,  0.0,  0.0],  # Typ 3 (neutral)
])

def compute_interaction_direction(pos_i, pos_j, type_i, type_j,
                                  matrix=INTERACTION_MATRIX,
                                  max_distance=50):

    delta = pos_j - pos_i
    distance = np.linalg.norm(delta)

    if distance == 0 or distance > max_distance:
        return np.zeros(2)

    # Richtung normieren
    direction = delta / distance

    # Stärke aus Matrix
    strength = matrix[type_i][type_j]

    # Effekt stärker, wenn Partikel nah sind
    factor = (1 - distance / max_distance)

    return direction * strength * factor




