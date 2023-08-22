# -----------------------------------------------------------------
# Decision Tree Classifier
# Predict the income of an adult based on the census data
# -----------------------------------------------------------------

# Import libraries
import pandas as pd


# Read dataset
df = pd.read_csv('./data/adultincome trunc.csv')


# Create Dummy variables
data_prep = pd.get_dummies(df, drop_first=True)


# Create X and Y Variables
X = data_prep.iloc[:, :-1]
Y = data_prep.iloc[:, -1]


# Split the X and Y dataset into training and testing set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = \
train_test_split(X, Y, test_size = 0.3, random_state = 1234, stratify=Y)


# Import and train Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(random_state=1234)


trained_model = rfc.fit(X_train, Y_train)


# Test the RFC model
Y_predict = rfc.predict(X_test)

# Evaluate the RFC model
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_predict)
score = rfc.score(X_test, Y_test)


# ---------------------------------------------------------------
# Create explanations for the model
# Make sure to install azureml-interpret azureml-explain-model
# ---------------------------------------------------------------

# Import the Tabular Explainer class
from interpret.ext.blackbox import TabularExplainer


# Define the Classes and features
classes  = ['Not Greater than 50K', 'Greater than 50K']
features = list(X.columns)


# Create the Tabular Explainer object
tab_explainer = TabularExplainer(trained_model,
                                 X_train,
                                 features=features,
                                 classes=classes)


# Get the global explanations
global_explanation = tab_explainer.explain_global(X_train)


# Get the feature importance data
global_fi = global_explanation.get_feature_importance_dict()

# Print the global feature importance values
for feature, importance in global_fi.items():
    print(feature,":", importance)


# Get Local feature importances
X_explain = X_test[0:5]


# Create Local explanations object
local_explanation = tab_explainer.explain_local(X_explain)

# Extract the feature names and corresponding importance values
local_features   = local_explanation.get_ranked_local_names()
local_importance = local_explanation.get_ranked_local_values()


# Print the local explanations
for i in range(0, len(local_features)):
    labels = local_features[i]
    print("\n Feature suppport values for : ", classes[i])
    
    for j in range(0, len(labels)):

        if Y_predict[j] == i:
            print("\n\tObservation number : ", j + 1)
            feature_names = labels[j]
            
            print("\t\t", "Feature Name".ljust(30), "  Value")
            print("\t\t", "-"*30, "-"*10)
            
            for k in range(0, len(feature_names)):
                print("\t\t", feature_names[k].ljust(30), round(local_importance[i][j][k], 6))

















