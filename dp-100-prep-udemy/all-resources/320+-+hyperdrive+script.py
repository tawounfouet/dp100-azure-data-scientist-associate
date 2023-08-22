# --------------------------------------------------------------
# Training Script for the Hyperdrive Job
# --------------------------------------------------------------

from azureml.core import Run

# Get the run context
new_run = Run.get_context()

# Get the workspace from the run
ws = new_run.experiment.workspace



# Get parameters
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--n_estimators", type=int)
parser.add_argument("--min_samples_leaf", type=int)
parser.add_argument("--input-data", type=str)

args = parser.parse_args()

ne = args.n_estimators
msl = args.min_samples_leaf



# --------------------------------------------------------
# Do your stuff here
# --------------------------------------------------------
import pandas as pd

# Load the data from the local files
df = new_run.input_datasets['raw_data'].to_pandas_dataframe()

# Select columns from the dataset
dataPrep = df.drop(['ID'], axis=1)

# Clean Missing Data - Drop the columns with missing values
dataPrep = dataPrep.dropna()


# Create Dummy variables - Not required in designer
dataPrep = pd.get_dummies(dataPrep, drop_first=True)

# Create X and Y - Similar to "edit columns" in Train Module
Y = dataPrep[['Default Next Month_Yes']]
X = dataPrep.drop(['Default Next Month_Yes'], axis=1)


# Split Data - X and Y datasets are training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = \
train_test_split(X, Y, test_size = 0.3, random_state = 1234, stratify=Y)


# Build the Random Forest model
from sklearn.ensemble import RandomForestClassifier as RFC

rfc = RFC(n_estimators=ne, min_samples_leaf=msl)


# Fit the data to the Random Forest object - Train Model
rfc.fit(X_train, Y_train)


# Predict the outcome using Test data - Score Model 
# Scored Label
Y_predict = rfc.predict(X_test)

# Get the probability score - Scored Probabilities
Y_prob = rfc.predict_proba(X_test)[:, 1]

# Get Confusion matrix and the accuracy/score - Evaluate
from sklearn.metrics import confusion_matrix
cm    = confusion_matrix(Y_test, Y_predict)
score = rfc.score(X_test, Y_test)


# Always log the primary metric
new_run.log("accuracy", score)

new_run.complete()






