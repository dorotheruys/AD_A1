import numpy as np


def get_theta_from_x(x_lst, chord):
    # Inputs:
    # list or array of x locations (not undimensionized with chord length [m]
    # chord length of airfoil
    # Output:
    # Array of theta points [rad]
    theta_lst = []
    for x in x_lst:
        theta = np.arccos(1 - 2 * x / chord)
        theta_lst.append(theta)
    return np.array(theta_lst)


def get_local_vorticity(AoA, Vinf, theta_lst):
    # Inputs:
    # list or array of theta locations [rad]
    # angle of attack [rad]
    # free stream velocity [m/s]
    # Output:
    # Array of vorticity at theta points
    vorticity_lst = []
    for theta in theta_lst:
        gamma = 2 * Vinf * AoA * (1 + np.cos(theta)) / np.sin(theta)
        vorticity_lst.append(gamma)
    vorticity_lst = np.array(vorticity_lst)
    vorticity_lst[0] = 0
    return vorticity_lst
