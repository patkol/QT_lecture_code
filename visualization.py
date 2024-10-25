from typing import Dict
import os
import numpy as np
import matplotlib.pyplot as plt

import constants as consts


def plot_device(device: Dict[str, np.ndarray], *, prefix: str="plots/", postfix: str=".svg"):
    """
    Plot all the device properties vs. x.
    """

    os.makedirs(prefix, exist_ok=True)

    fig, ax = plt.subplots()
    ax.plot(device["x"] / consts.NM, device["V_internal"] / consts.EV)
    ax.set_xlabel("x [nm]")
    ax.set_ylabel("V_internal [eV]")
    fig.savefig(prefix + "V_internal" + postfix)
