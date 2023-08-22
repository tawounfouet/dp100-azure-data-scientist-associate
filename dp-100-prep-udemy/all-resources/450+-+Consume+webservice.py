# -------------------------------------------------------------
# Consume the service end point using workspace access.
# -------------------------------------------------------------

# Import the Azure ML classes
from azureml.core import Workspace

# Access the workspace using config file
print("Accessing the workspace....")
ws = Workspace.from_config("./config")


# Access the service end points
print("Accessing the service end-points")
service = ws.webservices['adultincome-service']


# Prepare the input data
import json

x_new = {'age':[46],
         'wc':['Private'],
         'education':['Masters'],
         'marital status':['Married'],
         'race':['White'],
         'gender':['Male'],
         'hours per week':[60]}

# Convert the dictionary to a serializable list in json
json_data = json.dumps({"data": x_new})

# Call the web service
print("Calling the service...")
response = service.run(input_data = json_data)

# Collect and convert the response in local variable
print("Printing the predicted class...")
predicted_classes = json.loads(response)

print('\n', predicted_classes)




   
    
    