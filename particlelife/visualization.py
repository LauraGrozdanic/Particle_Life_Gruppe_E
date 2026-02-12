from vispy import scene
from vispy.app import Timer
import numpy as np
from .particles import Particles
from PyQt5.QtWidgets import QMainWindow


class Visualization(QMainWindow):
    """
    This Class makes a main window that visualizes and animates a particle simulation using VisPy.
    The update method advances the simulation by using the diffusion and wrap-around functions from the Particle class.
    """

    def __init__(self):
        super().__init__()

        self.canvas = scene.SceneCanvas(keys="interactive", show=False)
        self.canvas.title = "Particle Life"

        # Display the Vispy Scene inside the main window
        self.setCentralWidget(self.canvas.native)

        self.view = self.canvas.central_widget.add_view()
        self.view.camera = scene.cameras.PanZoomCamera(aspect=1)

        # Set boundaries for wrap-around
        self.xmin, self.xmax = -50, 50
        self.ymin, self.ymax = -50, 50

        # Frame the camera view to to show the simulation area
        self.view.camera.set_range(
            x=(self.xmin, self.xmax), y=(self.ymin, self.ymax), margin=0.05
        )

        # Make a particle system
        self.particles = Particles()

        x = self.particles.x
        y = self.particles.y

        types = self.particles.types
        face_colors = self.particles.colors[types]

        self.scatter = scene.visuals.Markers()

        # Make 2D array of positions with shape (N, 2)
        positions = np.column_stack((x, y))

        self.scatter.set_data(positions, face_color=face_colors, size=5)

        self.view.add(self.scatter)

        self.timer = Timer(interval=0.02, connect=self.update, start=True)

    def update(self, event):
        # move Particles
        x, y = self.particles.diffuse(0.2)

        # Use wrap around if Partcles go out of bounds
        self.particles.wrap_around(self.xmin, self.xmax, self.ymin, self.ymax)

        # set new positions after wrap around
        x, y = self.particles.x, self.particles.y

        positions = np.column_stack((x, y))
        types = self.particles.types
        face_colors = self.particles.colors[types]

        # update the visuals
        self.scatter.set_data(positions, face_color=face_colors, size=5)
