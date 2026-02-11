import numpy as np
from particlelife.particles import Particles


def test_wrap_around():
    p = Particles(n_points=3)

    # 3 Partikel absichtlich außerhalb setzen
    p.x = np.array([-5.0, 5.0, 15.0])
    p.y = np.array([-10.0, 0.0, 10.0])

    # linke und rechte Grenze setzen
    xmin, xmax = 0.0, 10.0
    # obere und untere Grenze setzen
    ymin, ymax = -5.0, 5.0

    p.wrap_around(xmin, xmax, ymin, ymax)

    # testen ob alle wieder im Bereich sind
    assert np.all(p.x >= xmin) and np.all(p.x < xmax)
    assert np.all(p.y >= ymin) and np.all(p.y < ymax)
