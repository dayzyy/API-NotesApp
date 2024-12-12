import json

USER_INSTANCES_PATH = './data/users.json'
USER_COUNT_PATH = './data/user_id_counter.txt'

class UserManager:
    @classmethod
    def load_database(cls):
        print('Loading up users...')

        try:
            open(USER_INSTANCES_PATH, 'r')
        except FileNotFoundError:
            with open(USER_INSTANCES_PATH, 'w') as file:
                json.dump({"users": []}, file)

            with open(USER_COUNT_PATH, 'w') as file:
                file.write('0')

    @classmethod
    def all(cls):
        with open('./data/users.json', 'r') as file:
            users_data = json.load(file)['users']

            users = []
            for user_data in users_data:
                users.append(User(**user_data))

            return users

    @classmethod
    def create(cls, username, password):
        with open('./data/user_id_counter.txt', 'r') as file:
            id = int(file.read())

        with open('./data/users.json', 'r') as file:
            data = json.load(file)
            data['users'].append({"id": id, "username": username, "password": password})

            with open('./data/users.json', 'w') as file:
                json.dump(data, file)

        with open('./data/user_id_counter.txt', 'w') as file:
            file.write(f'{id + 1}')
    
    @classmethod
    def DoesNotExist(cls, username):
        users = cls.all()

        for user in users:
            if username == user.username:
                return False
        return True
    
    # Checks if provided credentials (username and password) are valid (suitable for usage)
    @classmethod
    def validate(cls, username, password):
        if len(username) < 5:
            return False, 'Username must be at least 5 characters long'

        if len(password) < 5:
            return False, 'Password must be at least 5 characters long'

        return True, ''

class User:
    def __init__(self, id, username, password):
        self.id =  id
        self.username = username
        self.password = password

    objects =  UserManager

    def __str__(self):
        return self.username
