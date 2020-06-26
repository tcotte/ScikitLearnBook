import pandas as pd
import os


def load_housing_data(path, filename):
    csv_path = os.path.join(path, filename)
    return pd.read_csv(csv_path)
