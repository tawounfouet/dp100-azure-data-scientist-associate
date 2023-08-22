
from azureml.core import Run

# Get the run Context
new_run = Run.get_context()

# Get the workspace from. the run
ws = new_run.experiment.workspace

# --------------------------------------------------------------------------
# Do your stuff here 
# --------------------------------------------------------------------------

import pandas as pd 

# Read the input dataset 
df = new_run.input_datasets["raw_data"].to_pandas_dataframe()

# Load the data from the local files
#df = pd.read_csv("./data/loan.csv")

# Select the relevant columns from the dataset
dataPrep = df.drop(["Loan_ID"], axis=1)

all_cols = dataPrep.columns

# Check the missing values
dataNull = dataPrep.isnull().sum()

# Replace the missing values of string variable with mode
mode = dataPrep.mode().iloc[0]
cat_cols = dataPrep.select_dtypes(include='object').columns
dataPrep[cat_cols] = dataPrep[cat_cols].fillna(mode)

# Replace numerical columns with mean
num_cols = dataPrep.select_dtypes(include=['int', 'float']).columns
mean = dataPrep[num_cols].mean()
dataPrep[num_cols] = dataPrep[num_cols].fillna(mean)

# Create Dummy variables - Not Required in designer/classic studio
dataPrep = pd.get_dummies(dataPrep, drop_first=True)


# Normalise the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
columns = df.select_dtypes(include='number').columns
dataPrep[columns] = scaler.fit_transform(dataPrep[columns])


# Get the arguments from pipeline job
from argparse import ArgumentParser as AP

parser = AP()
parser.add_argument('--datafolder', type=str)
args = parser.parse_args()

# Create the folder if it doesn not exist
import os
os.makedirs(args.datafolder, exist_ok=True)


# Create the path
path = os.path.join(args.datafolder, 'defaults_prep.csv')

# Write the data prepation output as csv file
dataPrep.to_csv(path, index=False)


# Log null values
for column in all_cols:
    new_run.log(column, dataNull[column])

new_run.complete()



