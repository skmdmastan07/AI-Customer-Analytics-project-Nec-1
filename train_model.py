import pandas as pd
import pickle

from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

from utils.preprocessing import preprocess_data


# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("data/customers.csv")

# -----------------------------
# Customer Segmentation
# -----------------------------

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(
    df[["AnnualIncome", "SpendingScore"]]
)

# Save clustered data

df.to_csv(
    "data/customers_clustered.csv",
    index=False
)

# -----------------------------
# Purchase Prediction
# -----------------------------

df["Buy"] = (
    (df["AnnualIncome"] > 50000)
    &
    (df["SpendingScore"] > 50)
).astype(int)
processed_df = preprocess_data(df)

X = processed_df[
    [
        "Age",
        "AnnualIncome",
        "SpendingScore",
        "Gender"
    ]
]

y = processed_df["Buy"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# -----------------------------
# Save Model
# -----------------------------

with open(
    "models/purchase_model.pkl",
    "wb"
) as file:

    pickle.dump(model, file)

print("Model trained successfully!")
print("Clustered data saved.")
print("Model saved in models folder.")