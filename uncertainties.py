'''
This script contains functions for calculating uncertainties in microlensing events.
'''
from constants import a

def sigmaM_thetaE(
    M_L,
    theta_E,
    sigma_theta_E,
    #D_S,
    #D_L,
    #sigma_D_S,
    #sigma_D_L
):
    """
    Calculate the uncertainty in the mass of a microlensing event based on the Einstein radius and its uncertainty.
    
    Parameters:
    thetaE (float): The Einstein radius.
    sigma_thetaE (float): The uncertainty in the Einstein radius.
    D_S (float): The distance to the source.
    D_L (float): The distance to the lens.
    sigma_D_S (float): The uncertainty in the distance to the source.
    sigma_D_L (float): The uncertainty in the distance to the lens.
    M_L (float): The mass of the lens.

    Returns:
    float: The uncertainty in the mass.
    """
    # Calculate the uncertainty in the mass based on the Einstein radius and its uncertainty
    # sigma_M_theta = M_L * ((2 * sigma_theta_E / theta_E)**2 + (sigma_D_S)**2 * ((1 / D_S) - (1 / (D_S - D_L)))**2 + (sigma_D_L)**2 * (((1 / D_L) + 1 / (D_S - D_L)))**2)**0.5
    sigma_M_theta = M_L * (2 * sigma_theta_E / theta_E)
    return sigma_M_theta

def sigmaM_piE(
    M_L,
    pi_E,
    sigma_pi_E,
    #D_S,
    #D_L,
    #sigma_D_S,
    #sigma_D_L
):
    """
    Calculate the uncertainty in the mass of a microlensing event based on the parallax and its uncertainty.
    
    Parameters:
    piE (float): The parallax.
    sigma_piE (float): The uncertainty in the parallax.
    D_S (float): The distance to the source.
    D_L (float): The distance to the lens.
    sigma_D_L (float): The uncertainty in the distance to the lens.
    sigma_D_S (float): The uncertainty in the distance to the source.
    M_L (float): The mass of the lens.
    
    Returns:
    float: The uncertainty in the mass.
    """
    #sigma_M_pi = M_L * ((2 * sigma_pi_E / pi_E)**2 + (sigma_D_L)**2 * ((-1 / (D_S - D_L)) - (1 / D_L))**2 + (sigma_D_S)**2 * ((-1 / D_S) + (1 / (D_S - D_L)))**2)**0.5
    sigma_M_pi = M_L * (2 * sigma_pi_E / pi_E)
    return sigma_M_pi

def sigmaM_FL(
    M_L,
    F_L,
    sigma_F_L,
    #D_L,
    #sigma_D_L
):
    """
    Calculate the uncertainty in the mass of a microlensing event based on the flux and its uncertainty.
    
    Parameters:
    F_L (float): The flux.
    sigma_F_L (float): The uncertainty in the flux.
    D_L (float): The distance to the lens.
    sigma_D_L (float): The uncertainty in the distance to the lens.
    M_L (float): The mass of the lens.

    Returns:
    float: The uncertainty in the mass.
    """
    # Calculate the uncertainty in the mass based on the flux and its uncertainty
    sigma_M_FL = M_L * (sigma_F_L / (a * F_L))
    return sigma_M_FL