from fastapi import FastAPI
from src.api.schema import CreditRequest
from src.services.prediction_service import predict

app = FastAPI()


@app.post("/predict")
def get_prediction(data: CreditRequest):
    return predict(data)