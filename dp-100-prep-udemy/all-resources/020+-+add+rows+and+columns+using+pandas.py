# -----------------------------------------------
# Add columns and rows using Pandas
# -----------------------------------------------

import pandas as pd

# Add columns
df1 = pd.read_csv("./data/Employee Dataset - AC1.csv")
df2 = pd.read_csv("./data/Employee Dataset - AC2.csv")
df_ac = df1.join(df2)


# Add rows
df1 = pd.read_csv("./data/Employee Dataset - AR1.csv")
df2 = pd.read_csv("./data/Employee Dataset - AR2.csv")
df_ar = pd.concat([df1, df2], ignore_index=True)




















