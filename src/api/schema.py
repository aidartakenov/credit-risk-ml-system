from pydantic import BaseModel
from enum import Enum


class OccupationEnum(str, Enum):
    Journalist = "Journalist"
    Musician = "Musician"
    Accountant = "Accountant"
    Entrepreneur = "Entrepreneur"
    Developer = "Developer"
    Engineer = "Engineer"
    Media_Manager = "Media_Manager"
    Manager = "Manager"
    Mechanic = "Mechanic"
    Architect = "Architect"
    Doctor = "Doctor"
    Lawyer = "Lawyer"
    Scientist = "Scientist"
    Teacher = "Teacher"
    Writer = "Writer"


class CreditMixEnum(str, Enum):
    Good = "Good"
    Standard = "Standard"
    Bad = "Bad"


class PaymentMinEnum(str, Enum):
    Yes = "Yes"
    No = "No"


class PaymentBehaviourEnum(str, Enum):
    High_spent_Medium_value_payments = "High_spent_Medium_value_payments"
    Low_spent_Small_value_payments = "Low_spent_Small_value_payments"
    High_spent_Small_value_payments = "High_spent_Small_value_payments"
    Low_spent_Medium_value_payments = "Low_spent_Medium_value_payments"
    High_spent_Large_value_payments = "High_spent_Large_value_payments"
    Low_spent_Large_value_payments = "Low_spent_Large_value_payments"


class CreditRequest(BaseModel):

    Age: int
    Annual_Income: float
    Monthly_Inhand_Salary: float
    Num_of_Loan: int
    Total_EMI_per_month: float

    Occupation: OccupationEnum
    Credit_Mix: CreditMixEnum
    Payment_of_Min_Amount: PaymentMinEnum
    Payment_Behaviour: PaymentBehaviourEnum