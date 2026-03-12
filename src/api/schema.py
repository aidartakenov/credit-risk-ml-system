from pydantic import BaseModel

class CreditRequest(BaseModel):
    age: int
    income: float
    loan_amount: float
    employment_years: int
    employment_type: str  # можно добавить категории