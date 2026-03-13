import pandas as pd


def add_custom_features(X):

    X = X.copy()

    # безопасные фичи
    X["EMI_to_Income"] = (
        X["Total_EMI_per_month"] / X["Monthly_Inhand_Salary"]
    )

    X["Active_Loans"] = X["Num_of_Loan"]

    X["Occupation_CreditMix"] = (
        X["Occupation"].astype(str) + "_" + X["Credit_Mix"].astype(str)
    )

    return X