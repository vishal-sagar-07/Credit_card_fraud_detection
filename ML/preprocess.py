from schema.user_input import UserInput
import joblib
import pandas as pd
import numpy as np

feature_columns = joblib.load("model/feature_columns.pkl")

def preprocess(input: UserInput):
    data = {
        "amount": np.log1p(input.amount),
        "transaction_hour": input.transaction_hour,
        "foreign_transaction": int(input.foreign_transaction),
        "location_mismatch": int(input.location_mismatch),
        "device_trust_score": input.device_trust_score,
        "velocity_last_24h": input.velocity_last_24h,
        "cardholder_age": input.cardholder_age,
    }

    encoded_categories = {
        "merchant_category_Electronics": 0,
        "merchant_category_Food": 0,
        "merchant_category_Grocery": 0,
        "merchant_category_Travel": 0
    }

    if input.merchant_category != "Clothing":
        encoded_categories[
            f"merchant_category_{input.merchant_category}"
        ] = 1
        
    data.update(encoded_categories)

    input_df = pd.DataFrame([data])

    input_df = input_df[feature_columns]

    return input_df