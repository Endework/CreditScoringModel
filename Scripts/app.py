
from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# Load the model
model = joblib.load('XGBClassifier_model.pkl')

# Define the request body
class Transaction(BaseModel):
    TransactionId: int
    BatchId: int
    AccountId: int
    SubscriptionId: int
    CustomerId: int
    CountryCode: int
    ProviderId: int
    ProductId: int
    ChannelId: int
    Amount: float
    Value: float
    PricingStrategy: int
    TransactionHour: int
    TransactionDay: int
    TransactionMonth: int
    TransactionYear: int
    ProductCategory_data_bundles: int
    ProductCategory_financial_services: int
    ProductCategory_movies: int
    ProductCategory_other: int
    ProductCategory_ticket: int
    ProductCategory_transport: int
    ProductCategory_tv: int
    ProductCategory_utility_bill: int

@app.post("/predict")
def predict(transaction: Transaction):
    # Convert the request data to a DataFrame
    data = pd.DataFrame([transaction.dict().values()], columns=transaction.dict().keys())
    
    # Make a prediction
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    