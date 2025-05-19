# House Price Prediction Service

## Brief Description

This code implements a machine learning prediction API service for house price estimation. It loads a pre-trained regression model and exposes it via a Flask web server with two main endpoints: `/health` for service health checks and `/predict` for making predictions. The `/predict` endpoint accepts JSON input containing house features, validates the input using Pydantic, processes the data, and returns the predicted house price as a JSON response.

## Instructions for Running the Code and Tests

### 1. Set Up a Virtual Environment

It is recommended to use a Python virtual environment to isolate your project’s dependencies.

**Create a new virtual environment:**
```
python -m venv venv
```


**Activate the virtual environment:**

- On macOS/Linux:
    ```
    source venv/bin/activate
    ```
- On Windows:
    ```
    venv\Scripts\activate
    ```

### 2. Install Dependencies

Make sure you are in your project’s root directory (where `requirements.txt` is located), then run:
 ```
pip install -r requirements.txt
 ```
This will install all required packages for the project into your virtual environment.

### 3. Run the API Service

Start the Flask API by running:
 ```
 python app.py
  ```
 By default, the service will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### 4. Run the Tests



To execute the tests, run:
 ```
pytest --disable-warnings
 ```

### 5. Deployment
See considerations in [Docs folder](docs/).

#### Resources 
- https://medium.com/@anshitvishwa111/hosting-machine-learning-models-as-an-api-service-1cf5cb5a1e2f
- https://docs.pytest.org/en/stable/getting-started.html

