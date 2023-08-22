# -----------------------------------------------------
# Replace missing values from the dataset
# -----------------------------------------------------

import pandas as pd

df = pd.read_csv("./data/loan data.csv")

# Find out the missing values

df_null = df.isnull()

df_null2 = df.isnull().sum()


# Replacing/removing the rows with missing values
df_clean1 = df.dropna()



# Replace numeric columns with mean
# -----------------------------------------------
# Make copy of the original dataset
df_c = df.copy()

# Get the mean values of all the numeric columns
mean = df_c.mean()

# Replace the nan with mean
cols_num = ['LoanAmount', 'Loan_Amount_Term']

df_c[cols_num] = df_c[cols_num].fillna(mean)


df_c.isnull().sum()


# Replace categorical columns with Mode
# ----------------------------------------------------
cols_cat = ["Gender", "Married", "Dependents",
            "Self_Employed", "Credit_History"]

# Get the mode 
mode = df_c.mode().iloc[0]

# Replace the values using fillna
df_c[cols_cat] = df_c[cols_cat].fillna(mode)

df_c.isnull().sum()
















