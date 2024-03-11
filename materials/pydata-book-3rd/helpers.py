# conda create -n pydata-book-3rd python=3.10.13 anaconda
# conda activate pydata-book-3rd
# source deactivate
# conda remove -n pydata-book-3rd -all
import pandas as pd


def to_csv(df, path):
    df.loc[-1] = df.dtypes
    df.index = df.index + 1
    df.sort_index(inplace=True)
    df.to_csv(path, index=False)


def read_csv(path):
    dtypes = pd.read_csv(path, nrows=1).iloc[0].to_dict()
    return pd.read_csv(path, dtype=dtypes, skiprows=[1])