from typing import Dict
import numpy as np

import constants
import parameters as params


def get_hamiltonian(device: Dict[str, np.ndarray]):
    """
    Returns:
        H (Nx x Nx): The Hamiltonian
    """
    N = len(device["x"])
    T0 = constants.H_BAR**2 / 2 / params.X_STEP**2
    ms = device["m_eff"]
    Vs = device["V_internal"]

    H = np.zeros((N, N))  # OPTIM: make tridiagonal
    for i in range(1, N - 1):
        m_phdx = (ms[i] + ms[i + 1]) / 2
        m_mhdx = (ms[i - 1] + ms[i]) / 2
        H[i, i - 1] = -T0 / m_mhdx
        H[i, i + 1] = -T0 / m_phdx
        H[i, i] = T0 * (1 / m_phdx + 1 / m_mhdx) + Vs[i]

    H[0, 0] = T0 * 2 / ms[0] + Vs[0]
    H[1, 2] = -T0 / ms[0]
    H[-1, -1] = T0 * 2 / ms[-1] + Vs[-1]
    H[-1, -2] = -T0 / ms[-1]

    return H
