"""
This script contains the mass relations constrained by various obervables,
as well as the uncertainties propagated for these relations.

"""
# import the necessary libraries
import numpy as np

# import the necessary constants
from constants import kappa, a, A_b, M_0, L_0

def theta_E(M_L, D_L, D_S):
    """
    Calculate the Einstein radius based on the lens mass and distances.
    
    Parameters:
    M_L (float): Lens mass in solar masses
    D_L (float): Lens distance in kpc
    D_S (float): Source distance in kpc
    
    Returns:
    float: Einstein radius in arcseconds
    """
    theta_E = np.sqrt(kappa * M_L * (D_S - D_L) / (D_S * D_L))
    return theta_E

def pi_E(M_L, D_L, D_S):
    """
    Calculate the microlensing parallax based on the lens mass and distances.
    
    Parameters:
    M_L (float): Lens mass in solar masses
    D_L (float): Lens distance in kpc
    D_S (float): Source distance in kpc
    
    Returns:
    float: Microlensing parallax
    """
    pi_E = np.sqrt((D_S - D_L) / (kappa * M_L * D_S * D_L))
    return pi_E

def F_L(M_L, D_L):
    """
    Calculate the lens flux based on the lens mass and distance.
    
    Parameters:
    M_L (float): Lens mass in solar masses
    D_L (float): Lens distance in kpc
    
    Returns:
    float: Lens flux
    """
    F_L = ((L_0 * M_L**a) / (4 * np.pi * D_L**2)) * 10**(-0.4 * A_b)
    return F_L

def M_thetaE(theta_E, D_L, D_S):
    """
    Calculate the lens mass based on the Einstein radius and distances.
    
    Parameters:
    thetaE (float): Einstein radius in arcseconds
    D_L (float): Lens distance in kpc
    D_S (float): Source distance in kpc
    
    Returns:
    float: Lens mass in solar masses
    """
    M_L_theta = ((theta_E**2) / (kappa)) * (D_S * D_L / (D_S - D_L))
    return M_L_theta

def M_piE(pi_E, D_L, D_S):
    """
    Calculate the lens mass based on the microlensing parallax and distances.
    
    Parameters:
    piE (float): Microlensing parallax
    D_L (float): Lens distance in kpc
    D_S (float): Source distance in kpc
    
    Returns:
    float: Lens mass in solar masses
    """
    M_L_pi = ((D_S - D_L) / (D_S * D_L)) * (1 / (kappa * pi_E**2))
    return M_L_pi

def M_FL(D_L, F_L):
    """
    Calculate the lens mass based on the lens flux, 
    
    Parameters:
    M_L (float): Lens mass in solar masses
    D_L (float): Lens distance in kpc
    D_S (float): Source distance in kpc
    
    Returns:
    float: Lens mass in solar masses
    """
    M_L_FL = M_0 * ((4 * np.pi * F_L * D_L**2 * 10**(0.4*A_b)) / L_0)**(1/a) 
    return M_L_FL

def D_rel(D_L, D_S):
    """
    Calculate the relative distance between the lens and the source.
    
    Parameters:
    D_L (float): Lens distance in kpc
    D_S (float): Source distance in kpc
    
    Returns:
    float: Relative distance
    """
    D_rel = 1 / ((1 / D_L) - (1 / D_S))
    return D_rel

def pi_rel(D_rel):
    """
    Calculate the relative parallax based on the relative distance.
    
    Parameters:
    D_rel (float): Relative distance in kpc
    
    Returns:
    float: Relative parallax in arcseconds
    """
    pi_rel = 1 / D_rel
    return pi_rel