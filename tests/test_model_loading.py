import pickle
import os

def test_model_loading():
    model_path = "../ml/house_price_model.pkl"
    assert os.path.exists(model_path), "Model file does not exist"
    model = pickle.load(open(model_path, "rb"))
    assert model is not None, "Model failed to load"
