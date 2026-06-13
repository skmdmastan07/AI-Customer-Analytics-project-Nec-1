import pandas as pd
import numpy as np

np.random.seed(42)

rows = 200

customer_ids = np.arange(1, rows + 1)

genders = np.random.choice(
    ["Male", "Female"],
    size=rows
)

ages = np.random.randint(
    18,
    70,
    size=rows
)

annual_income = np.random.randint(
    15000,
    120000,
    size=rows
)

spending_score = np.random.randint(
    1,
    100,
    size=rows
)

df = pd.DataFrame({
    "CustomerID": customer_ids,
    "Gender": genders,
    "Age": ages,
    "AnnualIncome": annual_income,
    "SpendingScore": spending_score
})

df.to_csv(
    "data/customers.csv",
    index=False
)

print("Dataset created successfully!")
print(f"Total Rows: {len(df)}")