# -----------------------------------------------------
# Label Encoding of the categorical columns
# -----------------------------------------------------

import pandas as pd

df = pd.read_csv("./data/defaults.csv")
df = df.drop(["ID"], axis=1)

# Get the column names of the object/string type of columns
columns = df.select_dtypes(include='object').columns


# Change the object datatype to category
df[columns] = df[columns].astype("category")

# Check the datatype
df.dtypes

# Copy the dataframe
dt = df.copy()

# Drop the rows with missing values
dt = dt.dropna()

# Change the categorical columns to the numerical values
for column in columns:
    dt[column] = dt[column].cat.codes












