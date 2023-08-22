# -----------------------------------------------------
# Clip values or Remove outliers from the data
# -----------------------------------------------------

import pandas as pd

df = pd.read_csv("./data/loan data.csv")


df_clip = df[["ApplicantIncome"]].clip(999, 50000)


# Remove outliers using percentiles
df_ol = df.copy()

# Select the numeric column names
columns = df_ol.select_dtypes(include='number').columns

# Get the percentile 
for column in columns:
    lower = round(df_ol[column].quantile(0.01), 2) # 1%
    upper = round(df_ol[column].quantile(0.995), 2) # 99.5%
    print(column, lower, upper)
    df_ol[column] = df_ol[column].clip(lower, upper)
















