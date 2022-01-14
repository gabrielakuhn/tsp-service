import requests

api_url = "http://127.0.0.1:8000/api/location"
response = requests.get(api_url)
response.json()

print(response.json())
print(response.status_code)
