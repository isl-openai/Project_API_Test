import requests

url = "http://127.0.0.1:5000/users/2"

response = requests.get(url)

print("Status Code:", response.status_code)

print("Response JSON", response.json())