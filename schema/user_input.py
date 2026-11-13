from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Literal

#pydantic mmodel to validate incoming data
class UserInput(BaseModel):

    amount : Annotated[float, Field(..., description='Transaction Amount')]
    transaction_hour : Annotated[int, Field(..., ge=0, lt=24, description='Time of transaction')]
    merchant_category : Annotated[Literal['Electronics','Clothing','Grocery','Travel','Food'], Field(..., description='Category of transacttion', examples=['Electronics','Clothing','Grocery','Travel','Food'])]
    foreign_transaction : Annotated[bool, Field(..., description='True if transaction is foreign')]
    location_mismatch : Annotated[bool, Field(..., description='True if location not as registered one')]
    device_trust_score : Annotated[int, Field(...,ge=0, le=100, description='percentage  of trust score of the device being used for transaction')]
    velocity_last_24h : Annotated[int, Field(..., gt=0, description='Number of transactions in last 24hrs')]
    cardholder_age : Annotated[int, Field(...,gt=0, lt=100, description='Registered Age of the credit card holder')]

    @field_validator('merchant_category')
    @classmethod
    def normalize(cls, C : str):
        C = C.strip().title()
        return C