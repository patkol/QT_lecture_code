from typing import Sequence, Dict
import numpy as np


def get_device(xs: np.ndarray, *, boundaries: Sequence[float], **quantities: Sequence[float]) -> Dict[str, np.ndarray]:
    """
    xs: x-coordinates
    boundaries: Boundaries of the layers of the device
    quantities: Properties of the device, one entry per layer

    Returns:
        device: device[quantity_name] contains the corresponding device
                parameter as a function of x.
    """

    # Sanity checks
    assert np.all(xs[:-1] < xs[1:]), "xs is not sorted"
    assert xs[0] >= boundaries[0], "xs exceeds the left boundary of the device"
    assert xs[-1] <= boundaries[-1], "xs exceeds the right boundary of the device"
    for values in quantities.values():
        assert len(values) == len(boundaries) - 1, "More or less than one value per layer provided"

    # Initialize the device
    Nx = len(xs)
    device = dict((quantity_name, np.zeros(Nx)) for quantity_name in quantities.keys())
    device["x"] = np.copy(xs)

    layer_index = 0
    for x_index, x in enumerate(xs):
        # Update layer_index
        while x >= boundaries[layer_index + 1]:
            layer_index += 1
        for quantity_name, quantity_values in quantities.items():
            device[quantity_name][x_index] = quantity_values[layer_index]

    return device
