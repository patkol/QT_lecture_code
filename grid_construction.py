import numpy as np

import parameters as params


def get_grid(*, U_range: tuple[float, float], E_range: tuple[float, float], x_range: tuple[float, float]):
    """
    The grid is a dictionary containing the coordinates of all the dimensions (voltage, energy, position).
    """
    Us = np.arange(start=U_range[0], stop=U_range[1], step=params.U_STEP)
    Es = np.arange(start=E_range[0], stop=E_range[1], step=params.E_STEP)
    xs = np.arange(start=x_range[0], stop=x_range[1], step=params.x_STEP)
    grid = {'U': Us, 'E': Es, 'x': xs}

    return grid

