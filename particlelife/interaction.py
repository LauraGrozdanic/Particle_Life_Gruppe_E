# Interaktion zwischen partikeln

import numpy as np
from numba import njit

INTERACTION_MATRIX = np.array([
    #        0 (Türkis)  1 (Rot)   2 (Grün)  3 (Gelb)
        [-0.3,  0.2, -0.1,  0.4],
        [ 0.1, -0.3,  0.3, -0.2],
        [-0.4,  0.1, -0.3,  0.2],
        [ 0.3, -0.4,  0.2, -0.3],
])

@njit
def compute_forces(x, y, types, matrix, max_distance, interaction_strength):
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
#def compute_interaction_direction(pos_i, pos_j, type_i, type_j,
#                                  matrix=INTERACTION_MATRIX,
 #                                 max_distance=50,
  #                                interaction_strength=1.0):
#
 #   delta = pos_j - pos_i
  #  distance = np.linalg.norm(delta)
#
 #   if distance == 0 or distance > max_distance:
  #      return np.zeros(2)
#
 #   # Richtung normieren
  #  direction = delta / distance
#
 #   # Stärke aus Matrix
  #  strength = matrix[type_i][type_j] * interaction_strength


   # r = distance / max_distance

   # if r < 0.1:
   #     factor = -2.0 * (0.1 - r)        # starke Repulsion
    #elif r < 0.4:
     #   factor = 1.5 * (r - 0.1)         # Attraction
  #  elif r < 0.7:
   #     factor = -0.5 * (r - 0.4)        # leichte Repulsion
    #else:
     #   factor = 0.0
     
    #return direction * strength * factor



