from models import User

class UserSerializer:
    def __init__(self, users_data: list):
        users = []
        for data in users_data:
            try:
                 users.append(User(data['id'], data['username'], data['password']))
            except KeyError:
                 return None
        
        return users
