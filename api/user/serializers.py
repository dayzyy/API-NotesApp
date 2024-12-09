from user.models import User

class UserSerializer:
    def __init__(self, users_data, many=False):
        if not many:
            try:
                return User(users_data['id'], users_data['username'], users_data['password'])
            except KeyError:
                 return None

        users = []
        for data in users_data:
            try:
                 users.append(User(data['id'], data['username'], data['password']))
            except KeyError:
                 return None
        
        return users
