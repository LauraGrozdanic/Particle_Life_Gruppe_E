import numpy as np
from particlelife.interaction import compute_forces, INTERACTION_MATRIX


def test_forces_no_nan_():
    x = np.array([0.0, 0.0, 1.0])
    y = np.array([0.0, 0.0, 0.0])
    types = np.array([0, 1, 2], dtype=np.int64)
    max_distance = 10.0
    interaction_strength = 1.0

    fx, fy = compute_forces(
        x, y, types, INTERACTION_MATRIX, max_distance, interaction_strength
    )
    assert np.isfinite(fx).all()
    assert np.isfinite(fy).all()


def test_nointeraction_when_far():
    # Particles farther apart than max_distance should not interact.The resulting forces must be zero.
    x = np.array([0.0, 100.0])
    y = np.array([0.0, 0.0])
    types = np.array([0, 1], dtype=np.int64)
    max_distance = 10.0
    interaction_strength = 1.0
    fx, fy = compute_forces(
        x, y, types, INTERACTION_MATRIX, max_distance, interaction_strength
    )

    assert np.allclose(fx, 0.0)
    assert np.allclose(fy, 0.0)
