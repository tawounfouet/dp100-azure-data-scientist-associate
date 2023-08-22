# ------------------------------------------------------
# Understanding data conversion using JSON, 
# python dictionaries and Dataframe
# ------------------------------------------------------
import json
import pandas as pd

# Define a dictionary
d1 = {'name' : ['Jitesh'],
      'age'  : [40]}

# Create a JSON document
d1_j = json.dumps(d1)

# Load the JSON to dictionary
d2 = json.loads(d1_j)

# Convert the dictionary to a Dataframe
df1 = pd.DataFrame.from_dict(d1)











