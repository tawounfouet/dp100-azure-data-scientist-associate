# ------------------------------------------------------------
# Run a Hyperdrive Experiment in an Azureml environment
# ------------------------------------------------------------

# Import the Azure ML classes
from azureml.core import Workspace, Experiment

# Access the workspace using config.json
print("Accessing the workspace from job....")
ws = Workspace.from_config("./config")


# Get the input dataset
print("Accessing the Defaults dataset...")
input_ds = ws.datasets.get('Defaults')


# -------------------------------------------------
# Create custom environment
# -------------------------------------------------
from azureml.core import Environment
from azureml.core.environment import CondaDependencies

# Create the environment
myenv = Environment(name="MyEnvironment")

# Create the dependencies object
myenv_dep = CondaDependencies.create(conda_packages=['scikit-learn', 'pip'],
                                     pip_packages=['azureml-defaults'])

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

script_config = ScriptRunConfig(source_directory=".",
                                script="320 - hyperdrive script.py",
                                arguments = ['--input-data', input_ds.as_named_input('raw_data')],
                                environment=myenv,
                                compute_target=cluster)


# ---------------------------------------------------------------------
# Create Hyper drive parameters
# ---------------------------------------------------------------------

from azureml.train.hyperdrive import GridParameterSampling, choice

hyper_params = GridParameterSampling(
                {'--n_estimators': choice(10, 20, 50, 100),
                 '--min_samples_leaf': choice(1, 2, 5)
                 })


# ---------------------------------------------------------------------
# Configure the Hyperdrive class
# ---------------------------------------------------------------------
from azureml.train.hyperdrive import HyperDriveConfig, PrimaryMetricGoal

hyper_config = HyperDriveConfig(run_config=script_config,
                                hyperparameter_sampling=hyper_params,
                                policy=None,
                                primary_metric_name='accuracy',
                                primary_metric_goal=PrimaryMetricGoal.MAXIMIZE,
                                max_total_runs=20,
                                max_concurrent_runs=2)


# ---------------------------------------------------------------------
# Create the experiment and run
# ---------------------------------------------------------------------
new_experiment = Experiment(workspace=ws, name='Hyperdrive_Exp001')

new_run = new_experiment.submit(config=hyper_config)

new_run.wait_for_completion(show_output=True)


# ------------------------------------------------------------
# Best hyperdrive run with best combination of hyperparameter
# ------------------------------------------------------------
best_run = new_run.get_best_run_by_primary_metric()

print("Best Run ID : ", best_run.id)
print(best_run.get_metrics())














