# response  model
from pydantic import BaseModel,  Field
from typing import Annotated

class PredictionResponse(BaseModel):
    fraud : Annotated[bool, Field(..., description='prediction of model whether there is a fraud or not')]
    fraud_probability : Annotated[float, Field(..., description='percentage probability of fraud')] 