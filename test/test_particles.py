import numpy as np
from particlelife.particles import Particles


def test_wrap_around():
    p = Particles(n_points=3)

    # 3 Partikel absichtlich außerhalb setzen
    p.x = np.array([-5.0, -1.0, 15.0])
    p.y = np.array([-10.0, 0.0, 10.0])

    # linke und rechte Grenze setzen
    xmin, xmax = 0.0, 10.0
    # obere und untere Grenze setzen
    ymin, ymax = -5.0, 5.0

    p.wrap_around(xmin, xmax, ymin, ymax)

    # testen ob alle wieder im Bereich sind
    assert np.all(p.x >= xmin) and np.all(p.x < xmax)
    assert np.all(p.y >= ymin) and np.all(p.y < ymax)

def test_diffuse():
    # Erstellt 2 Partikel
    p = Particles(n_points=2)

    #feste Startposition (nichts ist random)
    p.x = np.array([0.0, 1.0])
    p.y = np.array([10.0, 20.0])

    # feste Geschwindigkeit
    p.vx = np.array([1.0, -2.0])
    p.vy = np.array([0.5, 0.0])

    # kein Zufallsrauschen, nur Bewegung durch vx/vy
    x_new, y_new = p.diffuse(n_step=0.0)

    expected_x = np.array([1.0, -1.0])
    expected_y = np.array([10.5, 20.0])

    # prüft ob es genau stimmt 
    assert (x_new == expected_x).all()
    assert (y_new == expected_y).all()