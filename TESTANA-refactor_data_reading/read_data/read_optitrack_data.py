import csv
import pandas as pd


def read_csv_file(file_path):
    # Initialize an empty list to store the data
    data = []

    # Open the CSV file
    with open(file_path, "r", newline="") as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Iterate over each row in the CSV file
        for row in reader:
            data.append(row)

    return data


def get_optitrack_flutter_data(dataset_path, key):
    optitrack_dict = dict()
    optitrack_dict["0"] = pd.DataFrame(
        read_csv_file(
            dataset_path
            + "/OptiTrack/LCO Measurements/Optitrack_LCO_onset_AoA_0_Config_1.csv"
        )
    )
    optitrack_dict["2"] = pd.DataFrame(
        read_csv_file(
            dataset_path
            + "/OptiTrack/LCO Measurements/Optitrack_LCO_onset_AoA_2_Config_1_001.csv"
        )
    )
    optitrack_dict["4"] = pd.DataFrame(
        read_csv_file(
            dataset_path
            + "/OptiTrack/LCO Measurements/Optitrack_LCO_onset_AoA_4_Config_1_002.csv"
        )
    )
    optitrack_dict["6"] = pd.DataFrame(
        read_csv_file(
            dataset_path
            + "/OptiTrack/LCO Measurements/Optitrack_LCO_onset_AoA_6_Config_1_003.csv"
        )
    )

    return optitrack_dict[key]


def get_optitrack_static_data(dataset_path, key):
    optitrack_dict = dict()
    optitrack_dict["-5"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_-5_18ms_018.csv"
        )
    )
    optitrack_dict["-4"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_-4_18ms_018.csv"
        )
    )
    optitrack_dict["-3"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_-3_18ms_019.csv"
        )
    )
    optitrack_dict["-2"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_-2_18ms_020.csv"
        )
    )
    optitrack_dict["-1"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_-1_18ms_021.csv"
        )
    )
    optitrack_dict["0"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_0_18ms.csv"
        )
    )
    optitrack_dict["1"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_1_18ms_022.csv"
        )
    )
    optitrack_dict["2"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_2_18ms_023.csv"
        )
    )
    optitrack_dict["3"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_3_18ms_024.csv"
        )
    )
    optitrack_dict["4"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_4_18ms_025.csv"
        )
    )
    optitrack_dict["5"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_5_18ms_026.csv"
        )
    )
    optitrack_dict["6"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_6_18ms_027.csv"
        )
    )
    optitrack_dict["7"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_7_18ms_028.csv"
        )
    )
    optitrack_dict["8"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_8_18ms_029.csv"
        )
    )
    optitrack_dict["10"] = pd.DataFrame(
        read_csv_file(
            dataset_path + "/OptiTrack/Static Deflections/Optitrack_AoA_10_18ms_030.csv"
        )
    )

    return optitrack_dict[key]



