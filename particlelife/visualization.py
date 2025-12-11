from vispy import app, scene
from vispy.app import Timer
import numpy as np
from .particles import Particles

from PyQt5.QtWidgets import QMainWindow

class Visualization(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
    
        self.canvas = scene.SceneCanvas(keys="interactive", show=True)
        self.canvas.title = "Particle Life"

        self.view = self.canvas.central_widget.add_view()

        self.view.camera = scene.cameras.PanZoomCamera(aspect=1)

        self.particles = Particles()
        x, y = self.particles.x, self.particles.y

        self.scatter = scene.visuals.Markers()
        self.scatter.set_data(np.array([x, y]).T, face_color="cyan", size=5)
        self.view.add(self.scatter)
        #app.run()


    def update(self, event):
        global x, y
        x, y = self.diffuse(x, y, 0.2)
        self.scatter.set_data(np.array([x, y]).T, face_color="cyan", size=5)
    
    
    timer = Timer(interval=0.02, connect=update, start=True)