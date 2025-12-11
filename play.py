from particlelife.visualization import Visualization
from vispy import app


if __name__ == "__main__":
    app.create()
    win = Visualization()
    win.show()
    app.run()
