import requests

URL = 'http://localhost:8080'

data = {
    "username": "an",
    "password": "paswwww",
}

response = requests.post(f'{URL}/register', json=data)

print(response.status_code, response.text)
