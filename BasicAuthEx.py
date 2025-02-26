import requests

url = "https://postman-echo.com/basic-auth"
response = requests.get(url, auth=("postman", "password"))

print(f"Status Code: {response.status_code}")
print(response.json())