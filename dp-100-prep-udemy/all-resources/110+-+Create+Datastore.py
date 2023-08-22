# -----------------------------------------------------
# Import the Workspace and Datastore class
# -----------------------------------------------------
from azureml.core import Workspace, Datastore


# -----------------------------------------------------
# Access the workspace from the config.json 
# -----------------------------------------------------
ws = Workspace.from_config(path="./config")


# -----------------------------------------------------
# Create a datastore 
# -----------------------------------------------------
az_store = Datastore.register_azure_blob_container(
            workspace=ws,
            datastore_name="azure_sdk_blob01",
            account_name="azuremlstb01",
            container_name="azuremlstb01blob",
            account_key="mQ6meDug7SdlFXu0/tBu7pKcNerxxYtO6X1V13M4sSohBAv2/i2KxdYe3ueiQXKrw+alPU1ou4NBuYBtuBVsig==")














