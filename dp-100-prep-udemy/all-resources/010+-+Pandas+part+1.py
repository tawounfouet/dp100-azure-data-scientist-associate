# -----------------------------------------------
# Use Pandas for data processing
# -----------------------------------------------

import pandas as pd

# Get the csv data using pandas
df = pd.read_csv("./data/loan data.csv")

# Read the tab delimited data
df_tab = pd.read_csv("./data/loan data tab.txt", sep='\t')


# Read the data from URL
columns = ["age", "wc", "fw", "edu", "edu_num",
           "ms", "occ", "rel", "race", "gender",
           "cg", "cl", "hpw", "nc", "income"]

df_h = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
                   header=None, #CSV has a header or not
                   names=columns)


# Select columns from the dataset - For Random selection
df_selected = df_h[["age", "income"]]

# Select columns using iloc - For larger datasets
df_iloc = df.iloc[0:5, 1:4]


# Select columns using negative index
X = df.iloc[:, :-1]

Y = df.iloc[:, -1:]


# drop columns from a dataframe
df_d = df.drop(["Loan_ID", "Gender"], axis=1) #Axis=0 for rows
















