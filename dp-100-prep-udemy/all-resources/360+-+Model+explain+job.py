# ------------------------------------------------------------
# Run an Experiment in an Azureml environment and 
# create and upload the explanations
# ------------------------------------------------------------

# Import the Azure ML classes
from azureml.core import Workspace, Experiment

# Access the workspace using config.json
print("Accessing the workspace from job....")
ws = Workspace.from_config("./config")


# Get the input dataset
print("Accessing the Adult Income dataset...")
input_ds = ws.datasets.get('AdultIncome')


# -------------------------------------------------
# Create custom environment
# -------------------------------------------------
from azureml.core import Environment
from azureml.core.environment import CondaDependencies

# Create the environment
myenv = Environment(name="MyEnvironment")

# Create the dependencies object
myenv_dep = CondaDependencies.create(conda_packages=['scikit-learn', 'pip'],
                                     pip_packages=['azureml-defaults', 'azureml-interpret'])

myenv.python.conda_dependencies = myenv_dep

# Register the environment
print("Registering the environment...")
myenv.register(ws)



# --------------------------------------------------------------------
# Create the compute Cluster 
# --------------------------------------------------------------------
# Specify the cluster name
cluster_name = "my-cluster-001"

# Provisioning configuration using AmlCompute
from azureml.core.compute import AmlCompute

print("Accessing the compute cluster...")

if cluster_name not in ws.compute_targets:
    print("Creating the compute cluster with name: ", cluster_name)
    compute_config = AmlCompute.provisioning_configuration(
                                     vm_size="STANDARD_D11_V2",
                                     max_nodes=2)

    cluster = AmlCompute.create(ws, cluster_name, compute_config)
    cluster.wait_for_completion()
else:
    cluster = ws.compute_targets[cluster_name]
    print(cluster_name, ", compute cluster found. Using it...")




# ---------------------------------------------------------------------
# Create a script configuration for custom environment of myenv
# ---------------------------------------------------------------------
from azureml.core import ScriptRunConfig

print("Creating the ScriptRunConfig....")
script_config = ScriptRunConfig(source_directory=".",
                                script="360 - Model explain script.py",
                                arguments = ['--input-data', input_ds.as_named_input('raw_data')],
                                environment=myenv,
                                compute_target=cluster)


# ---------------------------------------------------------------------
# Create the experiment and run
# ---------------------------------------------------------------------
print("Creating the experiment...")
new_experiment = Experiment(workspace=ws, name='Explainer_Exp001')

print("Submittting the experiment...")
new_run = new_experiment.submit(config=script_config)

new_run.wait_for_completion(show_output=True)












