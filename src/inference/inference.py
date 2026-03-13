import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print("Loading test data...")

df = pd.read_csv("data/raw/Credit_score_cleaned_data.csv")

X = df.drop(columns=["Credit_Score"])
y = df["Credit_Score"]

from sklearn.model_selection import train_test_split

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)
print("Loading trained model...")

model = joblib.load("models/pipeline_rf.pkl")

print("Running inference...")

y_pred = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Prediction distribution:")
print(np.unique(y_pred, return_counts=True))