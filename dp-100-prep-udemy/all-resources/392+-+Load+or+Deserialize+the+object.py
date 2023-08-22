# ---------------------------------------------------------
# Load the serialized object using joblib load
# ---------------------------------------------------------
# Import libraries
import pandas as pd

# Read dataset
data2 = pd.read_csv('./data/adultincome trunc.csv')


# Get the numeric columns from data2
columns = data2.select_dtypes(include='number').columns


# Load/Deserialize the object
import joblib
obj_file = './outputs/scaler.pkl'
sc = joblib.load(obj_file)


# Transform the data using the clone
data2[columns] = sc.transform(data2[columns])



