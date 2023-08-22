# Import required classes from Azureml
from azureml.core import Workspace, Datastore, Dataset, Experiment
from azureml.core import Run


# Access the Worspace, Datastore and Datasets
ws = Workspace.from_config("./config")
az_store = Datastore.get(ws, "azure_sdk_blob01")
az_dataset = Dataset.get_by_name(ws, "Loan Applications Using SDK")
az_default_store = ws.get_default_datastore()

# Get the context - data from the experience lunch on the submit script
new_run = Run.get_context()


# Do your stuff here
df = az_dataset.to_pandas_dataframe()

# Count the observations 
total_observations = len(df)

# Get the null/missing values
null_df = df.isnull().sum()



# Log metrics and Complet and experiment run
    # Log the metrics to the workspace
new_run.log("Total Observations", total_observations)

# Log the missing data values
for columns in df.columns:
    new_run.log(columns, null_df[columns])

new_run.complete()