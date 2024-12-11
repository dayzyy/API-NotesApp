import json

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

class Note:
    def __init__(self, id, body, created_at, status):
        self.id = id
        self.body = body
        self.created_at = created_at
        self.status = status

    objects = NoteManager
