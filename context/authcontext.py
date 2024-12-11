import requests

URL = 'http://localhost:8080'
SAVED_TOKEN_PATH = './context/token.txt'

def load_storage():
    try:
        open(SAVED_TOKEN_PATH, 'r')
    except FileNotFoundError:
        open(SAVED_TOKEN_PATH, 'w')

def saved_token():
    with open(SAVED_TOKEN_PATH, 'r') as file:
        return file.read()

def save_token(token):
    with open(SAVED_TOKEN_PATH, 'w') as file:
        return file.write(token)

def register(username, password):
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(f'{URL}/register', json=data)

    print(response.status_code, response.text)

def login(username, password):
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(f'{URL}/login', json=data)

    if response.status_code == 401:
        print(response.text)

    elif response.status_code == 200:

        data = response.json()

        print(response.status_code, data['text'])
        print(data['token'])

        save_token(data['token'])