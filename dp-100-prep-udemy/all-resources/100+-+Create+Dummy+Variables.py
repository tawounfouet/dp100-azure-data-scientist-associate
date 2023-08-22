# -----------------------------------------------------
# Hot Encoding of the categorical columns
# -----------------------------------------------------

import pandas as pd

df = pd.read_csv("./data/defaults.csv")
df = df.drop(["ID"], axis=1)

# Create Dummy variables 
df_dummy = pd.get_dummies(df)














