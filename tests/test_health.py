import requests

def test_health_check():
    url = 'http://127.0.0.1:5000/health'
    response = requests.get(url)
    assert response.status_code == 200
    assert "status" in response.json().get("message", "").lower()
