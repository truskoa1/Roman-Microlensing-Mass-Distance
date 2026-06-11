import numpy as np
import matplotlib.pyplot as plt

from constants import kappa
from mass_relations import F_L, M_FL, theta_E, pi_E, M_thetaE, M_piE
from fiducial_systems import systems

def plot_mass_relation(system_name, method="thetaE"):
    system = systems[system_name]

    # DL grid for the plot
    DL_grid = np.linspace(0.1, system["D_S"] - 0.01, 1000)

    # Defining the different combinations of observables to plot to constrain the lens mass
    if method == "thetaE_piE":

        thetaE_fid = theta_E(
            system["M_L"],
            system["D_L"],
            system["D_S"]
        )

        piE_fid = pi_E(
            system["M_L"],
            system["D_L"],
            system["D_S"]
        )

        M1 = M_thetaE(thetaE_fid, DL_grid, system["D_S"])
        M2 = M_piE(piE_fid, DL_grid, system["D_S"])

        title = r'$\theta_E$ and $\pi_E$ Constraints on Lens Mass'
             
    elif method == "thetaE_FL":
        thetaE_fid = theta_E(
            system["M_L"],
            system["D_L"],
            system["D_S"]
        )

        F_L_fid = F_L(
            system["M_L"],
            system["D_L"],   
        )

        M1 = M_thetaE(thetaE_fid, DL_grid, system["D_S"])
        M2 = M_FL(F_L_fid, DL_grid)

        title = r'$\theta_E$ and $F_L$ Constraints on Lens Mass'

    elif method == "piE_FL":
        piE_fid = pi_E(
            system["M_L"],
            system["D_L"],
            system["D_S"]
        )

        F_L_fid = F_L(
            system["M_L"],
            system["D_L"],   
        )

        M1 = M_piE(piE_fid, DL_grid, system["D_S"])
        M2 = M_FL(F_L_fid, DL_grid)

        title = r'$\pi_E$ and $F_L$ Constraints on Lens Mass'

    else:
        raise ValueError("method must be 'thetaE_piE', 'thetaE_FL or 'piE_FL'")

    # --- plot ---
    plt.figure()
    plt.plot(DL_grid, M1)
    plt.plot(DL_grid, M2)
    plt.xlim(0, system["D_S"] + 0.5)
    plt.ylim(0, 2)
    plt.grid()

    plt.xlabel(r'Lens Distance$D_L$ (kpc)')
    plt.ylabel(r'Lens Mass $M_L$ ($M_{\odot}$)')
    plt.title(title)
    plt.show()