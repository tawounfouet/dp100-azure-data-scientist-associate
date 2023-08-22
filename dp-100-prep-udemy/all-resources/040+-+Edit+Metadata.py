# -----------------------------------------------------
# Change the data type of a column
# -----------------------------------------------------

import pandas as pd

df = pd.read_csv("./data/loan data.csv")

# Get the data types
df.dtypes

# Change credit history to categorical
df["Credit_History"] = df["Credit_History"].astype("category")

















