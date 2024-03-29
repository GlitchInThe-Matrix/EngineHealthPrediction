# -*- coding: utf-8 -*-
"""Engine Health Prediction using Random Forest Classifier
"""

import pandas as pd
csv_path = '/content/engine_data.csv'  # Specify the path to your CSV file
df = pd.read_csv(csv_path)             # Read the CSV file into a Pandas DataFrame
df.head()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#Load the CSV dataset
df = pd.read_csv('engine_data.csv')

#Identify features (X) and target variable (y)
# Assuming the target variable is in a column named 'label'
X = df.drop('Engine Condition', axis=1)
y = df['Engine Condition']

#Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Create a Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

#Train the classifier on the training data
rf_classifier.fit(X_train, y_train)

#Make predictions on the testing data
y_pred = rf_classifier.predict(X_test)

#Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

#Print the results
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Classification Report:\n{classification_rep}")

#Testing
new_data = pd.read_csv('new_data.csv')
new_data_predictions = rf_classifier.predict(new_data)
print(new_data_predictions)