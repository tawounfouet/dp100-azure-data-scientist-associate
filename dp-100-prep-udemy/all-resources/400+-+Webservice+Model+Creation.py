# -----------------------------------------------------
# This script will submit the experiment run to the 
# local compute target and create the pkl files for
# column index object as well as the trained model.
# -----------------------------------------------------

# -----------------------------------------------------
# Import required classes from Azureml
# -----------------------------------------------------
from azureml.core import Workspace, Dataset, Experiment



# -----------------------------------------------------
# Access the Workspace and Datasets
# -----------------------------------------------------
print('Accessing the workspace....')
ws                = Workspace.from_config("./config")

print('Accessing the dataset....')
az_dataset        = Dataset.get_by_name(ws, 'AdultIncome')



# -----------------------------------------------------
# Create/Access an experiment object
# -----------------------------------------------------
print('Accessing/Creating the experiment...')
experiment = Experiment(workspace=ws, name='Webservice-exp001')



# -----------------------------------------------------
# Run an experiment using start_logging method
# -----------------------------------------------------
print('Start Experiment using Start Logging method...')
new_run = experiment.start_logging()



# --------------------------------------------------------
# Do your stuff here
# --------------------------------------------------------
import pandas as pd

# Load the data from the local files
print('Loading the dataset to pandas dataframe...')
df = az_dataset.to_pandas_dataframe()


# Create X and Y Variables
X = df.iloc[:, :-1]
Y = df.iloc[:, -1:]


# Create dummy variables
X = pd.get_dummies(X)


# Extract column names including dummy variables
train_enc_cols = X.columns


# Transform Categorical columns in Y dataset to dummy
Y = pd.get_dummies(Y)
Y = Y.iloc[:,-1]


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


# -------------------------------------------------------
# Save all the transformations and models
# -------------------------------------------------------
import joblib
model_file = './outputs/models.pkl'

joblib.dump(value=[train_enc_cols, trained_model], 
            filename=model_file)


# Complete the run
new_run.complete()


# Get the Run IDs from the experiment
list(experiment.get_runs())












