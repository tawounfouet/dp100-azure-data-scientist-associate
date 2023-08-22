# -----------------------------------------------------------------
# Register the model from workspace using run_id and local pkl file
# -----------------------------------------------------------------
from azureml.core import Workspace, Model


# Access the workspace using config.json
ws = Workspace.from_config("./config")


# Access the run using run_id
new_run = ws.get_run('<Your Run ID>')



# --------------------------------------------------------------------
# Register the model using the run object and uploaded pkl file
# --------------------------------------------------------------------
new_run.register_model(model_path='outputs/models.pkl', 
                       model_name='AdultIncome_models',
                       tags={'source':'SDK Run', 'algorithm':'RandomForest'},
                       properties={'Accuracy': new_run.get_metrics()['accuracy']},
                       description="Combined Models from Run")


# --------------------------------------------------------------------
# Register the model using Model Class and Local pkl file
# --------------------------------------------------------------------
from azureml.core import Model

Model.register(workspace=ws,
               model_path='./outputs/models.pkl', # local path
               model_name='AdultIncome_model_local',
               tags={'source':'SDK-Local', 'algorithm':'RandomForest'},
               properties={'Accuracy': 0.7866},
               description='AdultIncome model from Local'
               )


# --------------------------------------------------------------------
# Retrieve the registered models
# --------------------------------------------------------------------
Model.list(ws)


for model in Model.list(ws):
    
    print('\n', model.name, 'version:', model.version)
    print('\t', 'Run_ID : ', model.run_id)
    for prop_name in model.properties:
        prop = model.properties[prop_name]
        print ('\t',prop_name, ':', prop)
    
    for tags in model.tags:
        tag = model.tags[tags]
        print ('\t',tags, ':', tag)





