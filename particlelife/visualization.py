from vispy import app, scene
from vispy.app import Timer
import numpy as np
#from physics import diffuse
from .particles import Particles

class Visualization:
    def __init__(self):
    
        canvas = scene.SceneCanvas(keys="interactive", show=True)
        canvas.title = "Particle Life"

        view = canvas.central_widget.add_view()

        view.camera = scene.cameras.PanZoomCamera(aspect=1)

        particles = Particles()
        x, y = particles.x, particles.y

        scatter = scene.visuals.Markers()
        scatter.set_data(np.array([x, y]).T, face_color="cyan", size=5)
        view.add(scatter)
        #app.run()


    def update(self, event):
        global x, y
        x, y = diffuse(x, y, 0.2)
        self.scatter.set_data(np.array([x, y]).T, face_color="cyan", size=5)
    
    
    timer = Timer(interval=0.02, connect=update, start=True)