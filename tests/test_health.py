import requests

# Define the URL of your Flask API
url = 'http://127.0.0.1:5000/health'

# Send a GET request to the health endpoint
response = requests.get(url)

# Check the HTTP response status code
if response.status_code == 200:
    print("Health check passed")
    print("Response:", response.json())
else:
    print(f'Health check failed with status code: {response.status_code}')
    print(f'Response content: {response.text}')
