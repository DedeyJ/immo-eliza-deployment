from fastapi import FastAPI
import json
import pandas as pd
import uvicorn

from predict import make_prediction
from schema import PropertyInput
from predict import make_prediction

app = FastAPI()


# Endpoint to receive user input and return predictions
@app.get("/")
async def get_function():
    return {"running": "It's running"}


@app.post("/predict")
async def predict(data: PropertyInput):
    try:
        # Perform any necessary preprocessing on input data
        data_dict = data.dict()
        # Make predictions using the loaded model
        df = pd.json_normalize(data_dict)
        prediction = make_prediction(df)
        
        # Check if prediction is JSON serializable, if not, handle it
        json_serializable_prediction = prediction.tolist()
        return {"prediction": json_serializable_prediction[0]}
    except Exception as e:
        # Handle any exceptions that occur during prediction or serialization
        return {"error": str(e)}
    

