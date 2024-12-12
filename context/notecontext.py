import requests
import json

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
        print('Unauthorized! Log in to craete notes')
    elif response.status_code == 200:
        print(response.text)

def get_notes(filter=None):
    headers = {
        'Authorization': saved_token(),
    }

    data = {
        'filter': filter,
    }

    response = requests.get(f'{URL}', headers=headers, json=data)

    if response.status_code == 401:
        print('Unauthorized! Log in to access notes')
    elif response.status_code == 200:
        data = response.json()
        notes = json.loads(data)

        for note in notes:
            print(f'id: {note['id']} | date: {note['created_at']} | status: {note['status']} | "{note['body']}"')
