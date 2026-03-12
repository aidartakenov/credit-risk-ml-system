from src.api.schema import CreditRequest
from src.services.model_loader import model

def predict(data: CreditRequest):
    # Преобразуем данные в список фичей для модели
    features = [[
        data.age,
        data.income,
        data.loan_amount,
        data.employment_years
        # Можно добавить кодирование employment_type
    ]]
    pred = model.predict(features)
    prob = model.predict_proba(features)[0][1]  # вероятность одобрения

    return {
        "decision": "APPROVED" if pred[0] == 1 else "REJECTED",
        "probability": round(prob, 2)
    }