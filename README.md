## Functions

    'bandstructure': Find the eigenstates of the Hamiltonian with closed BC (mainly for quantum well)
    
    'transport', 'WF': Solve the SE with open BC. Determine the transmission and the DOS.
    
    'transport', 'NEGF': Find the Green's function to the SE with open BC. Determine the transmission and the DOS.
    
    'self_consistent': Do 'transport' and determine the density. Update the electrostatic potential and repeat. Determine the current.
    
    'scattering': NEGF with scattering in a self-consistent loop. No Poisson. Determine the density and the current.
    
    mode space code (exercises 7&8): 2D devices

## Building blocks

    Hamiltonian construction (calc_discrete_hamiltonian)
    
    Device construction (material.m)

## Plan
    + Device construction
    + Hamiltonian construction
    + bandstructure
    - scattering
    - transport NEGF (simplified scattering)
    - self_consistent
    - transport WF
    - 2D
