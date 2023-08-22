# -----------------------------------------------------
# Write the dataframe to a csv or a delimited file
# -----------------------------------------------------

import pandas as pd

df = pd.read_csv("./data/loan data.csv")


# Replacing/removing the rows with missing values
df_clean = df.dropna()

df_clean.to_csv("./data/cleaned loan data.txt",
                index=False, sep='\t')







