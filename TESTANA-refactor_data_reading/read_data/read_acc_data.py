import numpy as np
import scipy as sp
import pandas as pd
from pathlib import Path


def read_from_matlab(path):
    signal_mat = sp.io.loadmat(path)["Signal"]
    time_start = signal_mat["x_values"][0, 0][0, 0][0][0][0]
    time_step = signal_mat["x_values"][0, 0][0, 0][1][0][0]
    nr_of_values = signal_mat["x_values"][0, 0  ][0, 0][2][0][0]
    time_arr = time_start + np.arange(0, nr_of_values) * time_step
    acc_arr = signal_mat["y_values"][0, 0][0, 0][0]
    full_arr = np.vstack([time_arr, *acc_arr.transpose()]).transpose()
    full_dataframe = pd.DataFrame(full_arr, columns=["t", "M_x", "M_y", "M_z",
                                                     "U1_z", "U2_z", "U3_z", "U4_z",
                                                     "U5_z", "U6_z", "U7_z", "U8_z"])
    return full_dataframe


def get_acceleration_data(dataset_path):
    acc_dict = dict()
    acc_dict["0"] = read_from_matlab(dataset_path + "/Accelerometer data/Onset_LCO_AoA_0_Config_1_all_accel.mat")
    acc_dict["2"] = read_from_matlab(dataset_path + "/Accelerometer data/Onset_LCO_AoA_2_Config_1_all_accel.mat")
    acc_dict["4"] = read_from_matlab(dataset_path + "/Accelerometer data/Onset_LCO_AoA_4_Config_1_all_accel.mat")
    return acc_dict
