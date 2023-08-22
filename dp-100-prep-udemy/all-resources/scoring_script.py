import json
import joblib
from azureml.core.model import Model
import pandas as pd

# Called when the service is loaded
def init():
    global ref_cols, predictor
    
    # Get the path to the registered model file and load it
    model_path = Model.get_model_path('AdultIncome_models')
    ref_cols, predictor = joblib.load(model_path)


# Called when a request is received
def run(raw_data):
    # Get the input data as a dictionary
    data_dict = json.loads(raw_data)['data']
    
    # Convert dictionary to pandas dataframe
    data = pd.DataFrame.from_dict(data_dict)
    
    # Transform the data
    # data = one_hot.transform(data)
    
    data_enc = pd.get_dummies(data)

    deploy_cols = data_enc.columns

    # difference of train and deploy
    missing_cols = ref_cols.difference(deploy_cols)

    for cols in missing_cols:
        data_enc[cols] = 0

    data_enc = data_enc[ref_cols]

    # Get a prediction from the model
    predictions = predictor.predict(data_enc)
    
    classes = ['Less Than 50K', 'Greater Than 50K']
    
    predicted_classes = []
    
    for prediction in predictions:
        predicted_classes.append(classes[prediction])
    
    # Return the predictions
    return json.dumps(predicted_classes)





