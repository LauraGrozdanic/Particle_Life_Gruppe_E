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

The file interaction.py contains the logic for calculating the forces between particles. In this file, an interaction matrix is defined. This matrix describes how the four different particle types influence each other. Depending on the values in the matrix, particles either attract or repel each other. 

The main function in this file is compute_forces(). This function calculates the force components (fx, fy) acting on each particle. It computes the distance between particles, checks whether they are close enough to interact, applies the interaction rules from the matrix, and then returns the resulting forces for all particles. 

**Particle.py**

The file particles.py defines the Particles class and manages the whole particle system. It imports the force calculation from interaction.py so that particles can influence each other. 

In this file, the positions, velocities, types, and colors of all particles are stored. The file controls how the particles move over time. It updates their positions, changes their velocities based on interaction forces, and applies friction to slow them down gradually. 

It also makes sure that particles stay inside the simulation area. If a particle leaves one side of the area, it reappears on the opposite side. In addition, small random movement is added to simulate natural motion. 

**Visualization.py**

The file visualization.py is responsible for displaying and animating the particle simulation. It imports the Particles class to access the particle system. 
In this file, a main window is created and the simulation area is defined. The particles are displayed as colored points on the screen. The file continuously updates the simulation by applying the particle interactions, moving the particles, keeping them inside the boundaries, and refreshing their positions on the screen. This creates a smooth and continuous animation. 

**test files**
The test files check if the simulation works correctly and make sure that the main parts of the system behave as expected. 
There are two test files: test_interaction.py and test_particles.py. 
**test_interaction.py**

The file test_interaction.py tests the force calculation from interaction.py. It checks that the calculated forces do not contain invalid values like NaN or infinity. It also verifies that particles do not interact when they are too far apart. In that case, the forces must be zero. 

**test_particles.py**

The file test_particles.py tests the Particles class from particles.py. It checks the movement of particles, their interactions, and their boundary behavior. The tests make sure that particles stay inside the simulation area, that velocities remain the same when there is no force and no friction, and that velocities change when particles are close and interaction is active. 

## Running Tests 

```bash
# Run all tests
pytest

# Run linter
ruff check
```

