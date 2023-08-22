# ----------------------------------------------------------
# This script can be used as it is in the Azure Designer's
# Execute Python Scripts Module.
# 
# It expects an inpute dataset of AdultIncome.
# ----------------------------------------------------------

# Import libraries
import pandas as pd

# Define the mandatory azureml_main function with default None values
def azureml_main(dataframe1 = None, dataframe2 = None):
    df = dataframe1
    df = df.drop(['fw', 'edu_num'], axis=1)
    X = df.iloc[:, :-1]
    Y = df.iloc[:, -1:]
    return X, Y         # Return the dataframe object

