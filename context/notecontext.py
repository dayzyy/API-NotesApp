import requests
from context.authcontext import saved_token

URL = 'http://localhost:8080/notes'

def add(body):
    headers = {
        'Authorization': saved_token(),
    }

    data = {
        'body': body,
    }

    response = requests.post(f'{URL}/add', headers=headers, json=data)

    if response.status_code == 401:
        print('Unauthorized! Log into craete notes')
    elif response.status_code == 200:
        print(response.text)
