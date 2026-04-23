# src/services/prediction_service.py
import pandas as pd
from .model_loader import model
from src.database.db import log_prediction  # <- импортируем функцию логирования
import numpy as np

def predict(data):
    df = pd.DataFrame([data.dict()])
    
    prediction = model.predict(df)[0]

    # 👉 FIX 1: convert numpy → python type
    prediction = str(prediction)

    confidence = 0.0

    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(df)
        confidence = float(max(proba[0]))  # 👉 FIX 2

    # логирование
    log_prediction(data.dict(), prediction, confidence)

    return {
        "credit_score_prediction": prediction,
        "confidence": confidence
    }

def to_python_type(x):
    if isinstance(x, np.generic):
        return x.item()
    return x