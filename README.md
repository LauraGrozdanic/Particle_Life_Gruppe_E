# Particle Simulator

This project is a biology-inspired particle simulation that demonstrates emergent behavior through simple interaction rules. Thousands of particles of different types move, attract or repel each other and form visually complex patterns in real time.

This project was developed as part of the course Data Science & AI Infrastructures with a strong focus on professional Python software development.

![Demo](https://github.com/user-attachments/assets/9dfbaecb-e401-48e8-8ccc-b6517d86e899)

## How to run this simulation
### Prerequisites

- `Python 3.10 (or newer)`
- `VisPy`
- `PyQt5`
- `Numpy`
- `Numba`

Clone the repository:
```bash
git clone https://github.com/LauraGrozdanic/Particle_Life_Gruppe_E.git 
cd Particle_Life_Gruppe_E
```

Run the simulation:
```bash
python play.py
```

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
## Code Structure

<img width="548" height="743" alt="image" src="https://github.com/user-attachments/assets/8131fc77-4477-44b4-8c13-837e2185ff28" />


### Interaction.py
This file handles the force calculation between particles. It defines how particle types attract or repel each other and computes the resulting forces.

### Particle.py
This file defines and manages the particle system. It stores particle positions, velocities, types, and colors, updates their movement, applies interaction forces, adds friction, and ensures particles stay inside the simulation area.

### Visualization.py

This file is responsible for displaying and animating the simulation. It creates the window, shows the particles, and continuously updates their movement on the screen.

## Running Tests 

```bash
# Run all tests
pytest

# Run linter
ruff check
```

