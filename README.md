# Credit Card Fraud Detection API

A machine learning project that predicts whether a credit card transaction is fraudulent using a Random Forest classifier.

This project was built primarily as a learning exercise to gain hands-on experience with:

* Exploratory Data Analysis (EDA)
* Feature Engineering
* Machine Learning with Scikit-Learn
* FastAPI
* Pydantic Validation
* Docker
* ML Model Deployment Concepts

## Features

* Fraud prediction using a trained Random Forest model
* Input validation using Pydantic
* Custom preprocessing pipeline
* REST API built with FastAPI
* Health check endpoint
* Prediction confidence/probability score
* Dockerized application

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* FastAPI
* Pydantic
* Docker

## API Endpoints

### Home

GET /

Returns basic information about the API.

### Health Check

GET /health

Returns API health status and model version.

### Predict Fraud

POST /predict

Accepts transaction details and returns:

* Fraud prediction (True/False)
* Fraud probability (%)

## Example Response

```json
{
    "fraud": true,
    "fraud_probability": 68.6
}
```

## Project Structure

```text
.
├── app.py
├── Dockerfile
├── requirements.txt
├── models/
├── ml/
└── schema/
```

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Docker

Build image:

```bash
docker build -t fraud-api .
```

Run container:

```bash
docker run -p 8000:8000 fraud-api
```

## Disclaimer

This project was created for learning and educational purposes. It is not intended for production fraud detection and should not be used to make real financial decisions.
