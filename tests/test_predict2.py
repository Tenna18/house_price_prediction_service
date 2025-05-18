# tests/test_api_prediction.py

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    data = {
        "X1 transaction date": 2013.5,
        "X2 house age": 20.0,
        "X3 distance to the nearest MRT station": 250.5,
        "X4 number of convenience stores": 5,
        "X5 latitude": 24.947,
        "X6 longitude": 121.517
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "Predicted price" in response.get_json()
