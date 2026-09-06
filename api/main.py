from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load('../models/credit_risk_model.pkl')
feature_cols = joblib.load('../models/feature_columns.pkl')

@app.get("/")
def home():
    return {"message": "Credit Risk API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    for col in feature_cols:
        if col not in df.columns:
            df[col] = 0
    df = df[feature_cols]
    
    prob = float(model.predict_proba(df)[0][1])
    risk = "High" if prob > 0.5 else "Medium" if prob > 0.2 else "Low"
    
    return {"default_probability": round(prob, 3), "risk_category": risk}