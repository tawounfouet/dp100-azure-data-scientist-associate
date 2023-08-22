
# Import the Azure ML classes
from azureml.core import Workspace

# Access the workspace using config.json
print("Accessing the workspace from job....")
ws = Workspace.from_config("./config")


# -------------------------------------------------
# Create custom environment
# -------------------------------------------------
from azureml.core import Environment
from azureml.core.environment import CondaDependencies

# Create the environment
myenv = Environment(name="MyEnvironment")

# Create the dependencies object
print("Creating dependencies....")
myenv_dep = CondaDependencies.create(conda_packages=['scikit-learn', 'pip'],
                                     pip_packages=['azureml-defaults'])

myenv.python.conda_dependencies = myenv_dep

# Register the environment
print("Registering the environment...")
myenv.register(ws)



# -------------------------------------------------------------
# Create an Azure Kubernets Cluster
# -------------------------------------------------------------
from azureml.core.compute import AksCompute, ComputeTarget

cluster_name = 'aks-cluster-001'

if cluster_name not in ws.compute_targets:
    print(cluster_name, "does not exist. Creating a new one...")
    print('Creating provisioniong config for Aks cluster....')

    aks_config = AksCompute.provisioning_configuration(location='eastus',
                                                       vm_size='STANDARD_D11_V2',
                                                       agent_count=1,
                                                       cluster_purpose='DevTest')

    print("Creating the AKS Cluster...")
    production_cluster = ComputeTarget.create(ws, cluster_name, aks_config)
    production_cluster.wait_for_completion(show_output=True)
else:
    print(cluster_name, "exists. Using it...")
    production_cluster = ws.compute_targets[cluster_name]



# -------------------------------------------------
# Create Inference Configuration
# -------------------------------------------------
from azureml.core.model import InferenceConfig

print("Creating Inference Configuration...")
inference_config = InferenceConfig(source_directory = './service_files',
                                   entry_script="scoring_script.py",
                                   environment=myenv)


# -------------------------------------------------
# Create service deployment configuration
# -------------------------------------------------
from azureml.core.webservice import AksWebservice

print('Creating the Deployment configuration for webservice...')
deploy_config = AksWebservice.deploy_configuration(cpu_cores = 1,
                                                   memory_gb = 1)


# -------------------------------------------------
# Create and deploy the webservice
# -------------------------------------------------
from azureml.core.model import Model

model = ws.models['AdultIncome_models']

print('Deploying the web service....')
service = Model.deploy(workspace=ws,
                       name = 'adultincome-service',
                       models = [model],
                       inference_config = inference_config,
                       deployment_config = deploy_config,
                       deployment_target = production_cluster)

service.wait_for_deployment(show_output = True)











