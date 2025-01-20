#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt  # type: ignore

import parameters as params
from devices import device_properties_dict
import device_construction
import hamiltonian_construction
import visualization


device_properties = device_properties_dict[params.DEVICE_NAME]
E = 0.1  # TODO: energy range
eta = 1e-8  # Complex energy shift
xs = np.arange(
    start=device_properties["boundaries"][0],
    stop=device_properties["boundaries"][-1],
    step=params.X_STEP,
)
device = device_construction.get_device(xs, **device_properties)
visualization.plot_device(device)
H = hamiltonian_construction.get_hamiltonian(device)

Nx = len(xs)
# OPTIM: make use of sparsity
G_lesser = np.zeros((Nx, Nx))
G_greater = np.zeros((Nx, Nx))
G_retarded = np.zeros((Nx, Nx))

for born_index in range(1):
    # TODO: add scattering
    Sigma_retarded_scattering = np.zeros((Nx, Nx))

    G_retarded_inverted = (E + 1j * eta) * np.eye(Nx) - H - Sigma_retarded_scattering

    # Add boundary self-energies
    T_L = G_retarded_inverted[0, 1]
    T_R = G_retarded_inverted[-2, -1]
    D_L = G_retarded_inverted[0, 0]
    D_R = G_retarded_inverted[-1, -1]
    k_L = np.arccos(-D_L / (2 * T_L)) / params.X_STEP
    k_R = np.arccos(-D_R / (2 * T_R)) / params.X_STEP
    Sigma11 = -T_L * np.exp(1j * k_L * params.X_STEP)
    SigmaNN = -T_R * np.exp(1j * k_R * params.X_STEP)
    G_retarded_inverted[0, 0] -= Sigma11
    G_retarded_inverted[Nx - 1, Nx - 1] -= SigmaNN

    # OPTIM: RGF
    G_retarded = np.linalg.inv(G_retarded_inverted)

    # TODO: calculate the updated G_greater/lesser
