#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt  # type: ignore

import parameters as params
from devices import device_properties_dict
import device_construction
import hamiltonian_construction
import visualization


device_properties = device_properties_dict[params.DEVICE_NAME]
xs = np.arange(
    start=device_properties["boundaries"][0],
    stop=device_properties["boundaries"][-1],
    step=params.X_STEP,
)
device = device_construction.get_device(xs, **device_properties)
visualization.plot_device(device)
hamiltonian = hamiltonian_construction.get_hamiltonian(device)
energies, phis = np.linalg.eig(hamiltonian)  # Optim: use a tridiagonal solver
sorting_indices = np.argsort(energies)
energies = energies[sorting_indices]
phis = phis[:, sorting_indices]
print(np.sort(energies))
plt.plot(xs, phis[:, :3], label=energies[:3])
plt.legend()
plt.show()
