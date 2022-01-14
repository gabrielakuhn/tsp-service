import requests
import json

api_url = "http://127.0.0.1:8000/api/location"

# Data for test

json_file = open('api/requests/data_for_test.json')
json_str = json_file.read()
data = json.loads(json_str)


def main ():
    for i, value in enumerate(data):
        response = requests.post(api_url, json=value)
        response.json()
        print(value)
        print(response.status_code)

if __name__ == "__main__":
    main()
