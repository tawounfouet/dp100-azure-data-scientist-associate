# -----------------------------------------------------
# Data Normalization using MinMax and Standard Scalers
# -----------------------------------------------------
import pandas as pd

df = pd.read_csv("./data/defaults.csv")



# MinMaxScaler
dataminmax = df.copy()

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

columns = dataminmax.select_dtypes(include='number').columns
dataminmax[columns] = scaler.fit_transform(dataminmax[columns])




# Z-Score 
datastandard = df.copy()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

columns = datastandard.select_dtypes(include='number').columns
datastandard[columns] = scaler.fit_transform(datastandard[columns])
























