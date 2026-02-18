# Particle Simulator 

## Description
This project is a biology-inspired particle simulation that demonstrates emergent behavior through simple interaction rules. Thousands of particles of different types move, attract or repel each other and form visually complex patterns in real time.

This project was developed as part of the course Data Science & AI Infrastructures with a strong focus on professional Python software development.

![Demo](https://github.com/user-attachments/assets/9dfbaecb-e401-48e8-8ccc-b6517d86e899)


## Configuration 

This particle simulator does not have a GUI. The interactions can be modified in the interaction matrix.

```bash
  INTERACTION_MATRIX = np.array(
      [
          [-0.3, 0.2, -0.1, 0.4],  # Purple reacts to (Purple, Red, Green, Yellow)
          [0.1, -0.3, 0.3, -0.2],  # Red reacts to (Purple, Red, Green, Yellow)
          [-0.4, 0.1, -0.3, 0.2],  # Green reacts to (Purple, Red, Green, Yellow)
          [0.3, -0.4, 0.2, -0.3],  # Yellow reacts to (Purple, Red, Green, Yellow)
      ]
  )
```

The number of particles can be changed in the particle class n_point=number of particles

```bash
  class Particles: 
      def __init__(self, n_points=1000):
```

