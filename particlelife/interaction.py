# Interaktion zwischen partikeln

import numpy as np

INTERACTION_MATRIX = np.array([
    [ 0.0,  1.0, -1.0,  0.0],  # Typ 0 reagiert so auf 0,1,2,3
    [-1.0,  0.0,  1.0,  0.0],  # Typ 1
    [ 1.0, -1.0,  0.0,  0.0],  # Typ 2
    [ 0.0,  0.0,  0.0,  0.0],  # Typ 3 (neutral)
])




