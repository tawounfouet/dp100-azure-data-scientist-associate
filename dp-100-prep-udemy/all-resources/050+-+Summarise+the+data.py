# -----------------------------------------------------
# Summarise the data or Create summary statistics
# -----------------------------------------------------

import pandas as pd

df = pd.read_csv("./data/loan data.csv")

# Get the data types
df.dtypes

# Change credit history to categorical
df["Credit_History"] = df["Credit_History"].astype("category")


# Summarise the data
df_summary = df.describe(include='all', 
                         percentiles=[0.01, 0.05, 0.1, 0.9, 0.99, 0.995])















