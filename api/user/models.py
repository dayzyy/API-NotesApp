import json
from serializers import UserSerializer

USER_INSTANCES_PATH = './data/users.json'
USER_COUNT_PATH = './data/user_id_counter.txt'

class UserManager:
    @classmethod
    def load_database(cls):
        try:
            open(USER_INSTANCES_PATH, 'r')
        except FileNotFoundError:
            with open(USER_INSTANCES_PATH, 'w') as file:
                json.dump({"users": []}, file)

            with open(USER_COUNT_PATH, 'w') as file:
                file.write('0')

    @classmethod
    def all(cls):
        with open(USER_INSTANCES_PATH, 'r') as file:
            data = json.load(file)['users']
            users = UserSerializer(data)
            print()

    @classmethod
    def create(cls, username, password):
        pass

class User:
    def __init__(self, id, email, password):
        self.id =  id
        self.username = email
        self.password = password

    objects =  UserManager
