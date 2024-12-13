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

    @classmethod
    def all(cls):
        with open(NOTE_INSTANCES_PATH, 'r') as file:
            return json.load(file)['notes']

    @classmethod
    def filter(cls, username, status=None):
        notes = cls.all()
        demanded_notes = []
    
        if status is None:
            for note in notes:
                if note['username'] == username:
                    demanded_notes.append(note)

            return demanded_notes

        for note in notes:
            if note['status'] == status and note['username'] == username:
                demanded_notes.append(note)

        return demanded_notes

    @classmethod
    def remove(cls, username, id):
        notes = cls.filter(username=username)

        note_to_remove = notes[0]

        for note in notes:
            if int(note['id']) == id:
                note_to_remove = note
        
        notes = cls.all()
        notes.remove(note_to_remove)

        with open(NOTE_INSTANCES_PATH,  'w') as file:
            json.dump({"notes": notes}, file)

    @classmethod
    def update(cls, username, id, body=None, status=None):
        notes = cls.filter(username=username)
        
        updated_note = None
        if body is not None:
            for note in notes:
                if int(note['id']) == int(id):
                    note['body'] = body
                    updated_note = note

        if status is not None:
            for note in notes:
                if int(note['id']) == int(id):
                    note['status'] = status
                    updated_note = note

        if updated_note is None:
            raise ValueError('Note does not exist')

        all_notes = cls.all()

        for index, note in enumerate(all_notes):
            if note['id'] == updated_note['id']:
                all_notes[index] = updated_note

        with open(NOTE_INSTANCES_PATH, 'w') as file:
            json.dump({"notes": all_notes}, file)

    @classmethod
    def DoesNotExist(cls, username, id):
        notes = cls.filter(username=username)

        for note in notes:
            if int(note['id']) == id:
                return False

        return True


class Note:
    def __init__(self, id, body, created_at, status):
        self.id = id
        self.body = body
        self.created_at = created_at
        self.status = status

    objects = NoteManager
