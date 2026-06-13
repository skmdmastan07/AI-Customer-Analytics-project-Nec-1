from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):
    """
    Encode Gender column
    """

    df = df.copy()

    encoder = LabelEncoder()

    df["Gender"] = encoder.fit_transform(df["Gender"])

    return df