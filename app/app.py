import pandas as pd
import pickle
from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError, Field
import logging

# Load your model
model = pickle.load(open("../ml/house_price_model.pkl", "rb"))

# Initialize Flask app
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Define expected input schema
class HouseFeatures(BaseModel):
    X1_transaction_date: float = Field(..., alias="X1 transaction date")
    X2_house_age: float = Field(..., alias="X2 house age")
    X3_distance_to_mrt: float = Field(..., alias="X3 distance to the nearest MRT station")
    X4_convenience_stores: int = Field(..., alias="X4 number of convenience stores")
    X5_latitude: float = Field(..., alias="X5 latitude")
    X6_longitude: float = Field(..., alias="X6 longitude")

@app.route("/", methods=["GET"])
def index():
    return "Welcome to the House Price Prediction API"

@app.route("/health", methods=["GET"])
def health():
    return jsonify(message="status: OK")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Validate request input
        input_data = HouseFeatures(**request.json)
        logging.info(f"Received input: {input_data}") #logging request

        # Convert to DataFrame
        df = pd.DataFrame([input_data.dict(by_alias=True)])

        # Predict
        prediction = model.predict(df)
        logging.info(f"Prediction: {prediction.tolist()}") #logging response 

        return jsonify({"Predicted price": prediction.tolist()})

    except ValidationError as e:
        logging.error(f"Validation error: {e}")
        return jsonify(error="Invalid input", details=e.errors()), 400
    except Exception as e:
        logging.error(f"Internal error: {e}")
        return jsonify(error="Prediction failed", message=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)
