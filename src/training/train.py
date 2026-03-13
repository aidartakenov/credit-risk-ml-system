import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from src.utils.feature_engineering import add_custom_features
import joblib

# Loading the data
df = pd.read_csv("data/raw/Credit_score_cleaned_data.csv")

# Target and features
X = df.drop(columns=["Credit_Score"])
y = df["Credit_Score"]

# Categorical and numerical features
cat_features = ['Occupation', 'Credit_Mix', 'Payment_of_Min_Amount', 'Payment_Behaviour']
num_features = [
    'Age',
    'Annual_Income',
    'Monthly_Inhand_Salary',
    'Num_of_Loan',
    'Total_EMI_per_month'
]

# Creating new features

custom_features = ['Debt_to_Income', 'EMI_to_Income', 'Active_Loans', 'Occupation_CreditMix']

# Train / Val / Test split
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Pipeline
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1), cat_features)
])

pipeline = Pipeline([
    ('custom', FunctionTransformer(add_custom_features, validate=False)),
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(
        n_estimators=100,
        max_depth=None,
        max_features='sqrt',
        min_samples_split=6,
        random_state=42
    ))
])

# Training
pipeline.fit(X_train, y_train)

# Saving pipeline
os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, "models/pipeline_rf.pkl")

print("Pipeline trained and saved models/pipeline_rf.pkl")

# Testing on validation
y_val_pred = pipeline.predict(X_val)
from sklearn.metrics import classification_report
print("Validation Classification Report:")
print(classification_report(y_val, y_val_pred))

# Testing on inference
y_test_pred = pipeline.predict(X_test)
print("Test Classification Report:")
print(classification_report(y_test, y_test_pred))

print(df["Occupation"].unique())
print(df["Credit_Mix"].unique())
print(df["Payment_of_Min_Amount"].unique())
print(df["Payment_Behaviour"].unique())