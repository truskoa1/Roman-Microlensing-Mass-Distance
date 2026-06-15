import numpy as np
import matplotlib.pyplot as plt

from mass_relations import F_L, M_FL, theta_E, pi_E, M_thetaE, M_piE
from fiducial_systems import systems
from uncertainties import sigmaM_thetaE, sigmaM_piE

def plot_mass_relation(system_name, method):
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

        sigma_D_S = 0.1 * system["D_S"]
        sigma_D_L = 0.1 * DL_grid
        sigma_thetaE_fid = 0.1 * thetaE_fid
        sigma_piE_fid = 0.1 * piE_fid

        sigma1 = sigmaM_thetaE(
            M1,                    # mass array
            thetaE_fid,            # fixed theta_E
            sigma_thetaE_fid,      # uncertainty in theta_E
            system["D_S"],         # fixed D_S
            DL_grid,               # array of D_L values
            sigma_D_L,
            sigma_D_S               
        )

        sigma2 = sigmaM_piE(
            M2,                    # mass array
            piE_fid,               # fixed pi_E
            sigma_piE_fid,         # uncertainty in pi_E
            system["D_S"],         # fixed D_S
            DL_grid,               # array of D_L values
            sigma_D_L,
            sigma_D_S,
        )

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
        M2 = M_FL(DL_grid, F_L_fid)

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
        M2 = M_FL(DL_grid, F_L_fid)

        title = r'$\pi_E$ and $F_L$ Constraints on Lens Mass'

    elif method == "thetaE_knownDL":
        thetaE_fid = theta_E(
            system["M_L"],
            system["D_L"],
            system["D_S"]
        )

        D_L_fid = system["D_L"]

        M1 = M_thetaE(thetaE_fid, DL_grid, system["D_S"])

        title = r'$\theta_E$ and Known $D_L$ Constraints on Lens Mass'

    elif method == "piE_knownDL":
        piE_fid = pi_E(
            system["M_L"],
            system["D_L"],
            system["D_S"]
        )

        D_L_fid = system["D_L"]

        M1 = M_piE(piE_fid, DL_grid, system["D_S"])

        title = r'$\pi_E$ and Known $D_L$ Constraints on Lens Mass'

    elif method == "thetaE_piE_FL":
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

        F_L_fid = F_L(
            system["M_L"],
            system["D_L"],   
        )

        M1 = M_thetaE(thetaE_fid, DL_grid, system["D_S"])
        M2 = M_piE(piE_fid, DL_grid, system["D_S"])
        M3 = M_FL(DL_grid, F_L_fid)

        title = r'$\theta_E$, $\pi_E$, and $F_L$ Constraints on Lens Mass'
    
    elif method == "thetaE_piE_knownDL":
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

        D_L_fid = system["D_L"]

        M1 = M_thetaE(thetaE_fid, DL_grid, system["D_S"])
        M2 = M_piE(piE_fid, DL_grid, system["D_S"])

        title = r'$\theta_E$, $\pi_E$, and Known $D_L$ Constraints on Lens Mass'

    else:
        raise ValueError("method must be 'thetaE_piE', 'thetaE_FL or 'piE_FL'")

    # --- plot ---
    plt.figure()

    if method == "thetaE_knownDL" or method == "piE_knownDL":
        plt.plot(DL_grid, M1, label=r'$\theta_E$')
        plt.axvline(
        D_L_fid,
        color='orange',
        label=r'Known $D_L$'
    )
        
    elif method == "thetaE_piE_knownDL":
        plt.plot(DL_grid, M1, label=r'$\theta_E$')
        plt.plot(DL_grid, M2, label=r'$\pi_E$')
        plt.axvline(
        D_L_fid,
        color='green',
        label=r'Known $D_L$'
    )

    elif method == "thetaE_piE_FL":
        plt.plot(DL_grid, M1, label=r'$\theta_E$')
        plt.plot(DL_grid, M2, label=r'$\pi_E$')
        plt.plot(DL_grid, M3, label=r'$F_L$')

    elif method == "thetaE_piE":
        plt.plot(DL_grid, M1, label=r'$\theta_E$')
        plt.plot(DL_grid, M2, label=r'$\pi_E$')
        plt.fill_between(
        DL_grid,
        M1 - sigma1,
        M1 + sigma1,
        alpha=0.3,
        )

        plt.fill_between(
        DL_grid,
        M2 - sigma2,
        M2 + sigma2,
        alpha=0.3,
    )
    
    elif method == "thetaE_FL":
        plt.plot(DL_grid, M1, label=r'$\theta_E$')
        plt.plot(DL_grid, M2, label=r'$F_L$')

    elif method == "piE_FL":
        plt.plot(DL_grid, M1, label=r'$\pi_E$')
        plt.plot(DL_grid, M2, label=r'$F_L$')

    else:   
        plt.plot(DL_grid, M1)
        plt.plot(DL_grid, M2)
    
    plt.xlim(0, system["D_S"] + 0.5)
    plt.ylim(0, 2)
    plt.grid()

    plt.xlabel(r'Lens Distance $D_L$ (kpc)')
    plt.ylabel(r'Lens Mass $M_L$ ($M_{\odot}$)')
    plt.title(title)
    plt.legend(loc='upper right')
    plt.show()