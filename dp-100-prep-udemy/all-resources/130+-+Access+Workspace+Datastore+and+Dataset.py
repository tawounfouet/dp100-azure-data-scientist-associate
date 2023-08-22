# -----------------------------------------------------
# Import required classes from azureml
# -----------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset


# -----------------------------------------------------
# Access the workspace by name
# -----------------------------------------------------
ws = Workspace.from_config("./config")


# -----------------------------------------------------
# List all the workspaces within a subscription
# -----------------------------------------------------

ws_list = Workspace.list(subscription_id="77819c59-5764-4995-8596-d09cdc661078")
ws_list = list(ws_list)


# -----------------------------------------------------
# Access the default datastore from workspace
# -----------------------------------------------------
az_default_store = ws.get_default_datastore()


# -----------------------------------------------------
# List all the datastores
# -----------------------------------------------------
store_list = list(ws.datastores)


# -----------------------------------------------------
# Get the dataset by name from a workspace
# -----------------------------------------------------
az_dataset = Dataset.get_by_name(ws, "Loan Applications Using SDK")


# -----------------------------------------------------
# List datasets from a workspace
# -----------------------------------------------------

ds_list = list(ws.datasets.keys())

for items in ds_list:
    print(items)














