# ---------------------------------------------------------------
# Split the data for train and test
# ---------------------------------------------------------------

# Import pandas and read the file
import pandas as pd

df = pd.read_csv("./data/defaults.csv")

# Drop the ID column
df_prep = df.drop(["ID"], axis=1)


# Create Dummy variables 
df_prep = pd.get_dummies(df_prep, drop_first=True)


# Create the X and Y datasets
X = df_prep.drop(["Default Next Month_Yes"], axis=1)
Y = df_prep.iloc[:, -1:]


# Split the data
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, 
                                                    train_size=0.7,
                                                    random_state=1234,
                                                    stratify=Y)















