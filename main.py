from fastapi import FastAPI
from app_schema import Diagnosis
import pickle
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

with open("diabetes_prediction.pkl","rb") as model_file:
    model = pickle.load(model_file)
    print("MODELLLL",model)

app = FastAPI()
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {'message':'hello'}

@app.post("/predict")
def diabetes_diagnosis(data:Diagnosis):
    dataset = data.dict()
    
    result = []
    for item in dataset.items():
        result.append(item[1])
    
    data_array = np.asarray(result)
    reshaped_data = data_array.reshape(1,-1)
    prediction = model.predict(reshaped_data)
    
    if (prediction[0] == 0):
        return {"message":"This patient is not diabetic"}
    elif (prediction[0] == 2):
        return {"message":"This patient is predicted diabetic"}
    else:
        return {"message":"This patient is diabetic"}