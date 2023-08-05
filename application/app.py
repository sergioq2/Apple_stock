from fastapi import FastAPI
from pydantic import BaseModel
from prediction import prediction_model
import uvicorn
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['Apple_stock']
collection = db.prediction_collection

class AppleData(BaseModel):
    values: list = []

app = FastAPI()

@app.post("/predict")
def predict(data: AppleData):
    input_data = data.values
    
    if len(input_data) != 2:
        return {"error": "Invalid input. Expected a list of two values."}
    
    try:
        prediction = prediction_model(input_data)
        prediction_result = float(prediction)
        data_to_store = {"input": input_data, "output": prediction_result}
        collection.insert_one(data_to_store)

        return {"prediction": prediction_result}

    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}

@app.get("/history")
def history():
    history = list(collection.find({}, {"_id": 0}))
    return {"history": history}
