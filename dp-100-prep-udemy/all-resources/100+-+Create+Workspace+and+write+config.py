
# -----------------------------------------------------
# Import Workspace class 
# -----------------------------------------------------
from azureml.core import Workspace


# -----------------------------------------------------
#  Create the workspace
# -----------------------------------------------------
ws = Workspace.create(name='<Your Workspace Name>',
                      subscription_id='<Your Subscription ID>',
                      resource_group='<Resource group Name',
                      create_resource_group=True,   # True if it does not exist
                      location='<Nearest Azure region>')


# -----------------------------------------------------
# Write the config.json file to local directory
# -----------------------------------------------------

ws.write_config(path="./config")








