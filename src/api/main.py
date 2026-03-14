from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.schema import CreditRequest
from src.services.prediction_service import predict

app = FastAPI()

# Добавляем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # разрешаем все источники (для разработки)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Credit Risk API is running"}

@app.post("/predict")
async def get_prediction(data: CreditRequest):
    result = predict(data)
    return result