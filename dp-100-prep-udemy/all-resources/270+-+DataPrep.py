# -------------------------------------------------------------
# This script can be used as it is in the Azure Designer's
# Execute Python Scripts Module with the third zip bundle port.
#
# AdultIncome dataset must be uploaded the default datastore. 
# -------------------------------------------------------------

# Import the run class, Get context of the run and define workspace
from azureml.core import Run
new_run = Run.get_context()
ws = new_run.experiment.workspace

# Define a function to use inside the azureml_main function
def data_prep():
    input_ds = ws.datasets.get('AdultIncome').to_pandas_dataframe()
    input_ds = input_ds.drop(['fw', 'edu_num'], axis=1)
    input_ds = input_ds.iloc[:1000, :]
    return input_ds

