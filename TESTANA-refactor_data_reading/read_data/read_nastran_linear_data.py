import numpy as np


# Define a function to extract displacement vector data from .f06 file
def extract_displacement_vector_from_f06(file_path):
    # Initialize empty lists to store data
    point_id = []
    t1 = []
    t2 = []
    t3 = []
    # Open the .f06 file in read mode
    with open(file_path, 'r') as f:
        # Flag to start extracting data when relevant section is reached
        start_extraction = False

        # Iterate through each line in the file
        for line in f:
            # Check if the relevant section begins
            if line.strip().startswith("D I S P L A C E M E N T   V E C T O R"):
                # Set the flag to start extracting data
                start_extraction = True
                # Skip the header lines
                next(f)
                next(f)
                # Continue to the next iteration to skip the header line
                continue
            elif line.strip().startswith("S T R E S S E S   I N   B E A M   E L E M E N T S        ( C B E A M )"):
                break

            # Check if the relevant section ends
            if start_extraction and line.strip().startswith("MSC.NASTRAN"):
                # Break the loop if the end of section is reached
                break

            # If extraction has started, extract the data
            if start_extraction:
                # Split the line by whitespace
                line_data = line.split()
                # Check if line contains data (to skip empty lines or footer lines)
                if len(line_data) >= 7:
                    if any(elem != '0.0' for elem in line_data[2:5]) and line_data[2] != "AEROELASTIC" and line_data[
                    0] != "F" and line_data[0] != "POINT":
                        point_id.append((line_data[0]))
                        t1.append((line_data[2]))
                        t2.append((line_data[3]))
                        t3.append((line_data[4]))

    return point_id, t1, t2, t3


def get_nastran_linear_data(path):
    # Example usage
    point = int(input("Enter point you want to analyse: "))
    x = 0
    data_for_point = []
    while x < 10:

        file_path = "NASTRAN/f06 files/trim_delft_pazy_18ms_aoa_{}.f06".format(x + 1)

        point_id, t1, t2, t3 = extract_displacement_vector_from_f06(file_path)

        point_id = [int(i) for i in point_id]
        t1 = [float(i) for i in t1]
        t2 = [float(i) for i in t2]
        t3 = [float(i) for i in t3]

        i = 0
        displacement_data = {}
        while i < len(point_id):
            dataset = x + 1, t1[i], t2[i], t3[i]
            displacement_data.update({point_id[i]: dataset})
            i += 1

        data_for_point.append([displacement_data[point]])

        if x + 1 == 8:
            x += 2
        else:
            x += 1

    linear_dict = dict()

    print(["α: T1:           T2:           T3:         "])
    for i in range(9):
        print(data_for_point[i])

    return linear_dict  # todo have a dictionary of pandas dataframes for each angle of attack
