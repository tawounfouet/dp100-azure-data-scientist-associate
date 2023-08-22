# Databricks notebook source
try:
  dbutils.fs.unmount("/mnt/input")
except:
  print("Input Mount does not exist")

# COMMAND ----------

try:
  dbutils.fs.unmount("/mnt/output1")
except:
  print("Output Mount does not exist")

# COMMAND ----------

input_source = dbutils.widgets.get("input")
output1 = dbutils.widgets.get("testdata")

# COMMAND ----------

conf_key = "fs.azure.account.key.<your storage account name>.blob.core.windows.net"
key_value = "<Storage account access key>"

# COMMAND ----------

try: 
  dbutils.fs.mount(source = input_source,
                   mount_point = "/mnt/input",
                   extra_configs = {conf_key:key_value})
except:
  print('Input datastore already mounted...')

# COMMAND ----------

try:
  dbutils.fs.mount(source = output1,
                   mount_point = "/mnt/output1",
                   extra_configs = {conf_key:key_value})
except:
  print("Output data folder already mounted...")

# COMMAND ----------

import pandas as pd

# COMMAND ----------

df = pd.read_csv("/dbfs/mnt/input/adultincome trunc.csv")

# COMMAND ----------

# Create Dummy variables
data_prep = pd.get_dummies(df, drop_first=True)

# Create X and Y Variables
X = data_prep.iloc[:, :-1]
Y = data_prep.iloc[:, -1]

# Split the X and Y dataset into training and testing set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 1234, stratify=Y)

# COMMAND ----------

# Import and train Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(random_state=1234)

trained_model = rfc.fit(X_train, Y_train)

# Test the RFC model
Y_predict = rfc.predict(X_test)

# COMMAND ----------

dbutils.fs.mkdirs("/mnt/output1/000")

# COMMAND ----------

import joblib
obj_file = "/dbfs/mnt/output1/rfcModel.pkl"
joblib.dump(value=trained_model, filename=obj_file)

# COMMAND ----------

# Y_test, Y_predict

X_test.to_csv("/dbfs/mnt/output1/x_test.csv", index=False)

Y_test = pd.DataFrame(Y_test)
Y_test.to_csv("/dbfs/mnt/output1/y_test.csv", index=False)

Y_predict = pd.DataFrame(Y_predict)
Y_predict.to_csv("/dbfs/mnt/output1/y_predict.csv", index=False)
