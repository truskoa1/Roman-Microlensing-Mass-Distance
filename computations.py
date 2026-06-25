'''
This script contains the computations for derived quantities in microlensing. 

Parameters: 
    fiducial_system (str): The name of the fiducial system to compute derived quantities for.

Returns:
    dict: A dictionary containing the computed derived quantities for the specified fiducial system.

'''

from mass_relations import theta_E, pi_E, F_L, M_thetaE, M_piE, M_FL, D_rel, pi_rel
from fiducial_systems import systems

def compute_derived_quantities(M_L, D_L, D_S=8.0):

    theta_E_val = theta_E(M_L, D_L, D_S)
    pi_E_val = pi_E(M_L, D_L, D_S)
    F_L_val = F_L(M_L, D_L)
    M_thetaE_val = M_thetaE(theta_E_val, D_L, D_S)
    M_piE_val = M_piE(pi_E_val, D_L, D_S)
    M_FL_val = M_FL(D_L, F_L_val)
    D_rel_val = D_rel(D_L, D_S)
    pi_rel_val = pi_rel(D_rel_val)  

    derived_quantities = {
        'theta_E': theta_E_val,
        'pi_E': pi_E_val,
        'F_L': F_L_val,
        'M_thetaE': M_thetaE_val,
        'M_piE': M_piE_val,
        'M_FL': M_FL_val,
        'D_rel': D_rel_val,
        'pi_rel': pi_rel_val
    }

    return derived_quantities
