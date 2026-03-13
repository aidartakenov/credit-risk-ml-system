# src/services/prediction_service.py
import pandas as pd
from .model_loader import model
from src.database.db import log_prediction  # <- импортируем функцию логирования

def predict(data):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]

    # Если модель поддерживает predict_proba
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(df)
        confidence = max(proba[0])
    else:
        confidence = None

    # Логируем в базу
    log_prediction(data.dict(), prediction, confidence if confidence else 0.0)

    return {
        "credit_score_prediction": prediction,
        "confidence": confidence
    }