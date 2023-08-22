
# -----------------------------------------------------
# Import required azureml classes 
# -----------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset


# -----------------------------------------------------
# Access the workspace from the config.json 
# -----------------------------------------------------
ws = Workspace.from_config(path="./config")


# -----------------------------------------------------
# Access datastore by its name
# -----------------------------------------------------
az_store = Datastore.get(ws, "azure_sdk_blob01")


# -----------------------------------------------------
# Create and register the dataset
# -----------------------------------------------------

# Create the path of the csv file
csv_path = [(az_store, "Loan Data/Loan Approval Prediction.csv")]

# Create the dataset
loan_dataset = Dataset.Tabular.from_delimited_files(path=csv_path)

# Register the dataset
loan_dataset = loan_dataset.register(workspace=ws,
                                     name="Loan Applications Using SDK",
                                     create_new_version=True)











