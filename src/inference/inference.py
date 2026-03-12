import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print("Loading test data...")

X_test = pd.read_csv("data/processed/X_test.csv")
y_test = pd.read_csv("data/processed/y_test.csv").values.ravel()

print("Loading trained model...")

model = joblib.load("models/random_forest_model.pkl")

print("Running inference...")

y_pred = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))