import joblib

MODEL_PATH = "models/credit_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

# Загрузка модели один раз
model = load_model()