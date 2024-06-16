import os
import glob
import pandas as pd
dir_path = os.path.dirname(os.path.realpath(__file__))

def read_feather_files(directory):
    feather_files = glob.glob(os.path.join(directory, '**/*.feather'), recursive=True)
    for file in feather_files:
        try:
            df = pd.read_feather(file)
            print(f"Read file: {file}")
        except Exception as e:
            print(f"Error reading file {file}: {e}")
    return df

# # Example usage
# directory = f"{dir_path}/datasets"
# dataframes = read_feather_files(directory)
# print(type(dataframes))
# print(dataframes)

# --------------------