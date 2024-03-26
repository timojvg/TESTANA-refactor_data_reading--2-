import os
import pandas as pd


def NASTRAN_BASE(path):
    def floater(number_str):
        # print("Input_float =",number_str)
        value_correct = 1

        parts1 = number_str.split('.')
        # print(parts1)
        parts1_left = str(parts1[0])
        parts1_right = str(parts1[1])
        # Check for exponent
        if '-' in parts1_right:
            parts2 = parts1_right.split('-')
            Base_right = parts2[0]
            exp = parts2[1]
            # print("Parts 2 =",parts2)
            # print("Exp = ",exp)
            # print("Base_right =",Base_right)
        else:
            Base_right = parts1_right
            # print("Base_right =",Base_right)
            exp = 0
            # print("Exp = ",exp)

        # Check if before decimal point is empty
        if parts1_left == '':
            Base_left = 0
            # print("Base_left = ",Base_left)
        elif '-' in parts1_left:
            if parts1_left == '-':
                Base_left = 0
                # print("Base_left = ",Base_left)
            else:
                parts1_left_split = parts1_left.split('-')
                Base_left = parts1_left_split[1]
                # print("Base_left = ",Base_left)
        elif parts1_left[0] == '0' and parts1_right == '':
            value_correct = 0
            Base_left = 0
            Base_left = 0
        else:
            Base_left = parts1_left
            # print("Base_left = ",Base_left)

        # Sign for the float
        if '-' in parts1_left:
            sign = -1
            # print('Sign =' ,sign)
        else:
            sign = 1
            # print('Sign =' ,sign)

        # print("Parts1 =",parts1)
        # print("Value correct = ",value_correct)

        Corrected_float = float(value_correct) * float(sign) * float(
            str(Base_left) + '.' + str(Base_right)) * 10 ** float(-1 * float(exp))
        # print("Corrected_float =",Corrected_float)
        return Corrected_float

    file_path = path
    grid_found = False
    full_grid = []

    with open(file_path, "r") as file:
        for line in file:
            if line.startswith('GRID'):
                grid_found = True
                if grid_found:
                    line = line[0:48].strip()
                    # Split every 8 characters
                    n = 8
                    line = [line[i:i + n] for i in range(0, len(line), n)]
                    x = round(floater(line[3]), 10)
                    y = round(floater(line[4]), 10)
                    z = round(floater(line[5]), 10)
                    line = [x, y, z]
                    full_grid.append(line)
    return full_grid


def get_nastran_baseline_data(dataset_path):
    NASTRAN_dict = dict()
    NASTRAN_dict["1"] = pd.DataFrame(NASTRAN_BASE(dataset_path + "/Trim_Delft_Pazy_18ms_AoA_1.bdf"))
    NASTRAN_dict["2"] = pd.DataFrame(NASTRAN_BASE(dataset_path + "/Trim_Delft_Pazy_18ms_AoA_2.bdf"))
    NASTRAN_dict["3"] = pd.DataFrame(NASTRAN_BASE(dataset_path + "/Trim_Delft_Pazy_18ms_AoA_3.bdf"))
    NASTRAN_dict["4"] = pd.DataFrame(NASTRAN_BASE(dataset_path + "/Trim_Delft_Pazy_18ms_AoA_4.bdf"))
    NASTRAN_dict["5"] = pd.DataFrame(NASTRAN_BASE(dataset_path + "/Trim_Delft_Pazy_18ms_AoA_5.bdf"))
    NASTRAN_dict["6"] = pd.DataFrame(NASTRAN_BASE(dataset_path + "/Trim_Delft_Pazy_18ms_AoA_6.bdf"))
    NASTRAN_dict["7"] = pd.DataFrame(NASTRAN_BASE(dataset_path + "/Trim_Delft_Pazy_18ms_AoA_7.bdf"))
    NASTRAN_dict["8"] = pd.DataFrame(NASTRAN_BASE(dataset_path + "/Trim_Delft_Pazy_18ms_AoA_8.bdf"))
    NASTRAN_dict["10"] = pd.DataFrame(NASTRAN_BASE(dataset_path + "/Trim_Delft_Pazy_18ms_AoA_10.bdf"))

    return NASTRAN_dict
