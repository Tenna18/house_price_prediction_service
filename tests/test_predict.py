import requests
# Integration
def test_predict_endpoint():
    url = 'http://127.0.0.1:5000/predict'
    # Fictional data 
    data = {
        "X1 transaction date": 2013.5,
        "X2 house age": 20.0,
        "X3 distance to the nearest MRT station": 250.5,
        "X4 number of convenience stores": 5,
        "X5 latitude": 24.947,
        "X6 longitude": 121.517
    }
    response = requests.post(url, json=data)
    #  Endpoint accepts valid input and returns a 200 status.
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    json_response = response.json()
    # The response contains variable 
    assert "Predicted price" in json_response, "Prediction key missing in response"
    # The response is the correct instance type
    assert isinstance(json_response["Predicted price"][0], (float, int)), "Prediction is not float or int"

# Unit
def test_model_prediction_on_known_data():
    # Example input from training data
    features = [[2012.917, 32.0, 84.87882, 10, 24.98298, 121.54024]]
    expected_output = 37.9  

    # Load model
    import pickle
    with open("../ml/house_price_model.pkl", "rb") as f:
        model = pickle.load(f)

    
    #prediction = None
    prediction = model.predict(features)[0]
    assert prediction is not None, "prediction failed"

    # Allow for small floating point differences
    assert abs(prediction - expected_output) < 1e-2 #10 
