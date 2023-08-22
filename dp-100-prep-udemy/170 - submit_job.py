# Import the Azure Ml Classes
from azureml.core import Workspace, Experiment, ScriptRunConfig

# Access the workplace using config.json
ws = Workspace.from_config("./config")


new_experiment = Experiment(workspace=ws,
                           name="Loan_Script")

script_config = ScriptRunConfig(source_directory=".",
                               script="180 - Script To Run.py")

new_run = new_experiment.submit(config=script_config)


# Create a wait for completion of the script
new_run.wait_for_completion()