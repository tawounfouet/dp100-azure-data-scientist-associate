

# Import required classes from Azureml
from azureml.core import Run
import argparse

# Get parameters
parser = argparse.ArgumentParser()
parser.add_argument("--datafolder", type=str)
args = parser.parse_args()

# Get the context of the experiment run
new_run = Run.get_context()

# Acess the Workspace
ws = new_run.experiment.workspace




# --------------------------------------------------------------------------
# Do your stuff here 
# --------------------------------------------------------------------------
# Read th data from the previous step
import os 
import pandas as pd

path = os.path.join(args.datafolder, 'defaults_prep.csv')
dataPrep = pd.read_csv(path)

# Create X and y - Similar to "edit columns" in Train module
y = dataPrep["Loan_Status_Y"]
X = dataPrep.drop(columns=["Loan_Status_Y"], axis=1)

# Spit Data - X and y datasets are training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test =\
    train_test_split(X, y, test_size = 0.3, random_state = 1234, stratify=y)


# Build the Logistic Regression model
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()


# Fit the data to the LogisticRegression object - Train Model
lr.fit(X_train, y_train)


# Predict the outcome using Test data - Score Model 
# Scored Label
y_predict = lr.predict(X_test)

# Get the probability score - Scored Probabilities
y_prob = lr.predict_proba(X_test)[:, 1]

# Get Confusion matrix and the accuracy/score - Evaluate
from sklearn.metrics import confusion_matrix
cm    = confusion_matrix(y_test, y_predict)
score = lr.score(X_test, y_test)


# --------------------------------------------------------------------------
# Log metrics and Complete the experiment run
# --------------------------------------------------------------------------

# Create the confusion matrix dictionnary
cm_dict = {
            "schema_type": "confusion_matrix",
            "schema_version": "v1",
            "data": {"class_Labels": ["N", "Y"],
                     "matrix": cm.tolist()}
          }


# Create the Scored Dataset and upload to outputs
# -------------------------------------------------------
# Test Data - X_test
# Actual Y - y_test
# Scored label
# Scored probabilities

X_test = X_test.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)


y_prob_df = pd.DataFrame(y_prob, columns=["Scored Probabilities"])
y_predict_df = pd.DataFrame(y_predict, columns=["Scored Label"])

scored_dataset = pd.concat([X_test, y_test, y_predict_df, y_prob_df],
                           axis=1)
                        
# Upload the scored dataset
scored_dataset.to_csv("./outputs/defaults_scored.csv", index=False)


# Complete the run
new_run.complete()

       





