import json
from datetime import date

from user.models import User

NOTE_INSTANCES_PATH = './data/notes.json' 
NOTE_COUNT_PATH = './data/note_id_counter.txt'

class Status:
    todo = 'todo'
    inProgress = 'in-progress'
    done = 'done'

class NoteManager:
    @classmethod
    def load_database(cls):
        print('Loading up notes...')

        try:
            open(NOTE_INSTANCES_PATH, 'r')
        except FileNotFoundError:
            with open(NOTE_INSTANCES_PATH, 'w') as file:
                json.dump({"notes": []}, file)

            with open(NOTE_COUNT_PATH, 'w') as file:
                file.write('0')

    @classmethod
    def create(cls, username, body):
        if User.objects.DoesNotExist(username):
            raise ValueError(f'user with username {username} does not exist')

        with open(NOTE_COUNT_PATH, 'r') as file:
            id = file.read()
        
        created_at = date.isoformat(date.today())

        note = {
            "id": id,
            "created_at": created_at,
            "status": Status.todo,
            "body": body,
            "username": username,
        }

        with open(NOTE_INSTANCES_PATH, 'r') as file:
            data = json.load(file)

            data['notes'].append(note)

            with open(NOTE_INSTANCES_PATH, 'w') as file:
                json.dump(data, file)

        with open(NOTE_COUNT_PATH, 'w') as  file:
            file.write(f'{int(id) + 1}')

class Note:
    def __init__(self, id, body, created_at, status):
        self.id = id
        self.body = body
        self.created_at = created_at
        self.status = status

    objects = NoteManager
