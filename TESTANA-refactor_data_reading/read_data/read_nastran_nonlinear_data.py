import numpy as np


def get_nastran_nonlinear_data(path):
    # Specify the path to your .npy file
    npy_file = path + '/NASTRAN/Nonlinear_results/Converged_displacement_data_AoA_1_deg_V_18_0_ms.npy'

    # Load the .npy file
    data = np.load(npy_file)

    return data
