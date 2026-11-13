from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from ML.preprocess import preprocess
from ML.predict import predict_fraud, MODEL_VERSION
import numpy as np 

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "This is the homepage for the prediction model"}

@app.get("/about")
def about():
    return {"message": "We are building a REST API using FastAPI that loads a trained scikit-learn model and exposes one endpoint. A user sends their data as a JSON request, the model runs a prediction, and the API sends the result back as a JSON response. The model is trained on a real dataset. The whole thing is packaged inside a Docker container so it runs the same way everywhere, and deployed to a free cloud platform so it has a public URL."}

@app.get('/health')
def health_check():
    return {
        'status' : 'OK',
        'version': MODEL_VERSION
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(data: UserInput):

    try:
        processed_df = preprocess(data)

        result = predict_fraud(processed_df)

        return result
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

