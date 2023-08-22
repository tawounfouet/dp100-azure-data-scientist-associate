# --------------------------------------------------------------
# Training Script for the explainer Job
# --------------------------------------------------------------

from azureml.core import Run

# Get the run context
new_run = Run.get_context()


# Get the workspace from the run
ws = new_run.experiment.workspace


# Get parameters
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input-data", type=str)

args = parser.parse_args()




# --------------------------------------------------------
# Do your stuff here
# --------------------------------------------------------
import pandas as pd

# Load the data from the local files
df = new_run.input_datasets['raw_data'].to_pandas_dataframe()


# Create Dummy variables - Not required in designer
dataPrep = pd.get_dummies(df, drop_first=True)


# Create X and Y Variables
X = dataPrep.iloc[:, :-1]
Y = dataPrep.iloc[:, -1]


# Split Data - X and Y datasets are training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = \
train_test_split(X, Y, test_size = 0.3, random_state = 1234, stratify=Y)


# Build the Random Forest model
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(random_state=1234)

# Fit the data to the Random Forest object - Train Model
trained_model = rfc.fit(X_train, Y_train)


# Predict the outcome using Test data - Score Model 
Y_predict = rfc.predict(X_test)

# Get the probability score - Scored Probabilities
Y_prob = rfc.predict_proba(X_test)[:, 1]

# Get Confusion matrix and the accuracy/score - Evaluate
from sklearn.metrics import confusion_matrix
cm    = confusion_matrix(Y_test, Y_predict)
score = rfc.score(X_test, Y_test)


# Always log the primary metric
new_run.log("accuracy", score)

# Get explanation
from interpret.ext.blackbox import TabularExplainer

features = list(X.columns)
classes = ['notGreater', 'Greater']

tab_explainer = TabularExplainer(trained_model, 
                              X_train, 
                              features=features, 
                              classes=classes)

explanation = tab_explainer.explain_global(X_train)


# Upload the explanations to the workspace
from azureml.interpret import ExplanationClient

# Create explanation client
explain_client = ExplanationClient.from_run(new_run)

# Upload the explanations
explain_client.upload_model_explanation(explanation,
                                        comment="My First Explanations")


# Complete the run
new_run.complete()

















