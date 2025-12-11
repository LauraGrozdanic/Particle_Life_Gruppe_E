from vispy import app, scene
from vispy.app import Timer
import numpy as np
from .particles import Particles
from PyQt5.QtWidgets import QMainWindow


class Visualization(QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = scene.SceneCanvas(keys="interactive", show=True)
        self.canvas.title = "Particle Life"

        self.view = self.canvas.central_widget.add_view()
        self.view.camera = scene.cameras.PanZoomCamera(aspect=1)

        # Partikel
        self.particles = Particles()
        x = self.particles.x
        y = self.particles.y

        types = self.particles.types
        face_colors = self.particles.colors[types]

        # DEBUG
        print("x shape:", x.shape)
        print("y shape:", y.shape)
        print("combined shape:", np.column_stack((x, y)).shape)


        self.scatter = scene.visuals.Markers()

        positions = np.column_stack((x, y))   # Shape (N, 2) → korrekt für VisPy

        self.scatter.set_data(
            positions,
            face_color=face_colors,
            size=5
        )

        self.view.add(self.scatter)

        self.timer = Timer(interval=0.02, connect=self.update, start=True)

    def update(self, event):
        # Partikel bewegen
        x, y = self.particles.diffuse(0.2)

        positions = np.column_stack((x, y))  # wieder (N, 2)
        types = self.particles.types
        face_colors = self.particles.colors[types]
        # Visual aktualisieren
        self.scatter.set_data(
            positions,
            face_color=face_colors,
            size=5
        )
