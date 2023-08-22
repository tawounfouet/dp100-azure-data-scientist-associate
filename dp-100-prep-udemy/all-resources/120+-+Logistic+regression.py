# ---------------------------------------------------------------
# Perform logistic regression on the defaults.csv dataset
# ---------------------------------------------------------------

import pandas as pd

# Load the data from the local files
df = pd.read_csv("./data/defaults.csv")


# Select relevant columns from the dataset
dataPrep = df.drop(["ID"], axis=1)


# Check the missing values
dataNull = dataPrep.isnull().sum()


# Replace the missing values of string variable with mode
mode = dataPrep.mode().iloc[0]
cols = dataPrep.select_dtypes(include='object').columns

dataPrep[cols] = dataPrep[cols].fillna(mode)


# Replace numerical columns with mean
mean = dataPrep.mean()
dataPrep = dataPrep.fillna(mean)


# Create Dummy variables - Not required in designer/Classic Studio
dataPrep = pd.get_dummies(dataPrep, drop_first=True)



# Normalise the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
columns = df.select_dtypes(include='number').columns
dataPrep[columns] = scaler.fit_transform(dataPrep[columns])


# Create X and Y - Similar to "edit columns" in Train Module
Y = dataPrep[['Default Next Month_Yes']]
X = dataPrep.drop(['Default Next Month_Yes'], axis=1)


# Split Data - X and Y datasets are training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = \
train_test_split(X, Y, test_size = 0.3, random_state = 1234, stratify=Y)


# Build the Logistic Regression model
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()


# Fit the data to the LogisticRegression object - Train Model
lr.fit(X_train, Y_train)


# Predict the outcome using Test data - Score Model 
# Scored Label
Y_predict = lr.predict(X_test)


# Get the probability score - Scored Probabilities
Y_prob = lr.predict_proba(X_test)[:, 1]



# Get Confusion matrix and the accuracy/score - Evaluate
from sklearn.metrics import confusion_matrix
cm    = confusion_matrix(Y_test, Y_predict)
score = lr.score(X_test, Y_test)












