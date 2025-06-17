from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from datetime import datetime

# Load saved model and encoder
city_encoder = joblib.load("models/city_encoder.pkl")
model = joblib.load("models/Risk_Classifier.pkl")

app = FastAPI(title="Crime Risk Predictor")

# Input schema
class CrimeInput(BaseModel):
    city: str
    age: int
    gender: int  # Assuming 0 for Male, 1 for Female

@app.get("/")
def home():
    return {"message": "Welcome to the Crime Risk Level Prediction API"}

@app.post("/predict/")
def predict_risk(data: CrimeInput):
    try:
        # Encode city
        if data.city not in city_encoder.classes_:
            return {"error": f"Unknown city: {data.city}"}

        encoded_city = city_encoder.transform([data.city])[0]

        # Get current time
        now = datetime.now()
        current_hour = now.hour
        current_month = now.month

        # Prepare input for model
        input_df = pd.DataFrame([{
            "City": encoded_city,
            "Age": data.age,
            "Gender": data.gender,
            "Hour": current_hour,
            "Month": current_month
        }])

        # Predict
        prediction = model.predict(input_df)[0]
        return {
            "predicted_risk_level": str(prediction),
            "details": {
                "City": data.city,
                "Age": data.age,
                "Gender": data.gender,
                "Hour": current_hour,
                "Month": current_month
            }
        }
    
    except Exception as e:
        return {"error": str(e)}
