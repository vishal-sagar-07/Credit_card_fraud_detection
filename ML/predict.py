import joblib

model = joblib.load("model/fraud_rf_model.pkl")
MODEL_VERSION = '1.0.0'

def predict_fraud(input_df):

    prediction = model.predict(input_df)

    probability = model.predict_proba(input_df)

    return {
        "fraud": bool(prediction[0]),
        "fraud_probability": round(
            probability[0][1] * 100,
            2
        )
    }