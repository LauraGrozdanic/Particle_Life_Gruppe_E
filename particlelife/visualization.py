from vispy import app, scene
from vispy.app import Timer
import numpy as np
from physics import diffuse

    
canvas = scene.SceneCanvas(keys="interactive", show=True)
canvas.title = "Particle Life"

view = canvas.central_widget.add_view()

view.camera = scene.cameras.PanZoomCamera(aspect=1)

n_points = 1000
x = np.random.normal(loc=0.0, scale=10.0, size=n_points)
y = np.random.normal(loc=0.0, scale=10.0, size=n_points)

scatter = scene.visuals.Markers()
scatter.set_data(np.array([x, y]).T, face_color="cyan", size=5)
view.add(scatter)


def update(event):
    global x, y
    x, y = diffuse(x, y, 0.2)
    scatter.set_data(np.array([x, y]).T, face_color="cyan", size=5)
    
    
timer = Timer(interval=0.02, connect=update, start=True)


if __name__ == "__main__":
    app.run()