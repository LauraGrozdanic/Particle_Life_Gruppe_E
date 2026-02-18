# Particle Simulator 

## Description
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
## Code Structure Description
The project is divided into several Python modules. Each module has a specific task, and together they form the complete simulation. 

In this report, we focus on the test files and the modules inside the Particle Life directory. The simulation is started through play.py, which runs the whole system. 

The Particle Life directory contains the main code of the simulation. It includes three modules: interaction.py, particles.py, and visualization.py. These files are connected through imports and work together to run the simulation. 

**Interaction.py**

This file handles the force calculation between particles. It defines how particle types attract or repel each other and computes the resulting forces.

**Particle.py**

This file defines and manages the particle system. It stores particle positions, velocities, types, and colors, updates their movement, applies interaction forces, adds friction, and ensures particles stay inside the simulation area.

**Visualization.py**

This file is responsible for displaying and animating the simulation. It creates the window, shows the particles, and continuously updates their movement on the screen.

**test files**
The test files ensure that the simulation works correctly. test_interaction.py verifies the force calculation and checks that no interaction happens when particles are too far apart. test_particles.py verifies particle movement, boundary behavior, and interaction logic.

 

## Running Tests 

```bash
# Run all tests
pytest

# Run linter
ruff check
```

