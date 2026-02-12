from vispy import scene
from vispy.app import Timer
import numpy as np
from .particles import Particles
from PyQt5.QtWidgets import QMainWindow


class Visualization(QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = scene.SceneCanvas(keys="interactive", show=False)
        self.canvas.title = "Particle Life"

        self.setCentralWidget(self.canvas.native) #canvas in das hauptfenster eingesetzt

        self.view = self.canvas.central_widget.add_view()
        self.view.camera = scene.cameras.PanZoomCamera(aspect=1)

        #Grenzen setzen für wrap around
        self.xmin, self.xmax = -50, 50
        self.ymin, self.ymax = -50, 50

        #fenster anpassen(kein rauszoomen mehr nötig)
        self.view.camera.set_range(
            x=(self.xmin, self.xmax),
            y=(self.ymin, self.ymax),
            margin=0.05
        )

        # Partikel
        self.particles = Particles()

        x = self.particles.x
        y = self.particles.y

        types = self.particles.types
        face_colors = self.particles.colors[types]

        self.scatter = scene.visuals.Markers()

        positions = np.column_stack((x, y))   # Shape (N, 2) → korrekt für VisPy

        self.scatter.set_data(
            positions,
            face_color=face_colors,
            size=5
        )

        self.view.add(self.scatter)

        self.timer = Timer(interval=0.01, connect=self.update, start=True)

    def update(self, event):

        self.particles.apply_interactions(
            max_distance=50,
            interaction_strength=0.04,
            friction=0.995
        )

        # Partikel bewegen
        x, y = self.particles.diffuse(0.01)

        #warp around an den Rändern anwenden
        self.particles.wrap_around(self.xmin, self.xmax, self.ymin, self.ymax)

        #gibt die aktuelle Positionnen nach dem Wrap around wieder
        x, y = self.particles.x, self.particles.y

        positions = np.column_stack((x, y))  # wieder (N, 2)
        types = self.particles.types
        face_colors = self.particles.colors[types]
        # Visual aktualisieren
        self.scatter.set_data(
            positions,
            face_color=face_colors,
            size=5
        )
