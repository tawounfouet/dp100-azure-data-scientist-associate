
# -----------------------------------------------------
# Import required classes from Azureml
# -----------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset


# -----------------------------------------------------
# Access the Workspace, Datastore and Datasets
# -----------------------------------------------------
ws                = Workspace.from_config("./config")
az_store          = Datastore.get(ws, 'azure_sdk_blob01')
az_dataset        = Dataset.get_by_name(ws, 'Loan Applications Using SDK')
az_default_store  = ws.get_default_datastore()


# -----------------------------------------------------
# Upload local files to storage account using datastore 
# -----------------------------------------------------
files_list = ["./data/test.csv", "./data/test1.csv"]

az_store.upload_files(files=files_list,
                      target_path="Loan Data/",
                      relative_root="./data/",
                      overwrite=True)


# -----------------------------------------------------
# Upload folder or directory to the storage account
# -----------------------------------------------------
az_store.upload(src_dir="./data",
                target_path="Loan Data/data",
                overwrite=True)














