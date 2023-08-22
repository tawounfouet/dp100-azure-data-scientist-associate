
# ------------------------------------------------------------
# Run a script in an Azureml environment
# ------------------------------------------------------------
# This code will submit the script provided in ScriptRunConfig
# and create an Azureml environment on the local machine
# including docker for Azureml
# -------------------------------------------------------------


# Import the Azure Ml Classes
from azureml.core import Environment
from azureml.core.environment import CondaDependencies
from azureml.core import Workspace, Experiment, ScriptRunConfig

# Access the workplace using config.json
ws = Workspace.from_config("./config")

# Create/access the experiment from workspace
new_experiment = Experiment(workspace=ws,
                            name="Training_Script")

# --------------------------------------------------------
# Create custom environment

myenv = Environment(name="MyEnvironment")

# Create the dependencies object
myenv_dep = CondaDependencies.create(conda_packages=["scikit-Learn"])
myenv.python.conda_dependencies = myenv_dep

myenv.register(ws)
# --------------------------------------------------------

script_config = ScriptRunConfig(source_directory=".",
                                script="200 - Training Script.py",
                                environment=myenv)

# Submit a new run using the ScriptRunConfig
new_run = new_experiment.submit(config=script_config)
