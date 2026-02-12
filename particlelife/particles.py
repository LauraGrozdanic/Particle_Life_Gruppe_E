import numpy as np
from .interaction import compute_interaction_direction

class Particles:
    def __init__ (self, n_points=300):
        self.n_points = n_points
        self.x = np.random.normal(loc=0.0, scale=10.0, size=n_points)
        self.y = np.random.normal(loc=0.0, scale=10.0, size=n_points)
        
        

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
        self.x += np.random.normal(scale=n_step, size=self.x.shape)
        self.y += np.random.normal(scale=n_step, size=self.y.shape)

        self.x += self.vx
        self.y += self.vy
        return self.x, self.y
    
    def apply_interactions(self,
                           max_distance=50,
                           interaction_strength=1.0,
                           friction=0.95):
        
        n = self.n_points
        positions = np.column_stack((self.x, self.y))

        for i in range(n):
            total_force = np.zeros(2)

            for j in range(n): 
                if i == j: 
                    continue

                total_force += compute_interaction_direction(
                    positions[i],
                    positions[j],
                    self.types[i],
                    self.types[j],
                    max_distance=max_distance,
                    interaction_strength=interaction_strength
                )

            self.vx[i] += 0.01 * total_force[0]
            self.vy[i] += 0.01 * total_force[1]

        #Reibung
        self.vx *= friction
        self.vy *= friction

    
    #wenn PArtikel den Rand verlassen, kommen sie auf der gegenüberliegenden Seite wieder
    def wrap_around(self, xmin, xmax, ymin, ymax):
        width = xmax - xmin
        height = ymax - ymin

        self.x = ((self.x - xmin) % width) + xmin
        self.y = ((self.y - ymin) % height) + ymin
