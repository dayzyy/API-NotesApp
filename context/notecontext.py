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

def delete(id):
    headers = {
        'Authorization': saved_token()
    }

    data = {
        'id': id
    }

    response = requests.post(f'{URL}/remove', headers=headers, json=data)

    if response.status_code == 401:
        print('Unauthorized! Log in to modify notes')
    elif response.status_code == 404:
        print(f'Note with id: [{id}] doesnt not exist (or is not yours)')
    elif response.status_code == 200:
        print(f'Note successfuly deleted!')

def update(id, body=None, status=None):
    headers = {
        'Authorization': saved_token()
    }

    if body is not None:
        data = {
            'id': id,
            'body': body
        }
    else:
        data = {
            'id': id,
            'status': status
        }

    response = requests.post(f'{URL}/update', headers=headers, json=data)

    if response.status_code == 401:
        print('Unauthorized! Log in to modify notes')
    elif response.status_code == 404:
        print(f'Note with id: [{id}] doesnt not exist (or is not yours)')
    elif response.status_code == 200:
        print(f'Note successfuly updated!')
