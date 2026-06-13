import pandas as pd
import os


def load_data(filepath):
    """
    Load CSV file safely
    """

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    return pd.read_csv(filepath)


def save_data(df, filepath):
    """
    Save dataframe safely
    """

    df.to_csv(filepath, index=False)