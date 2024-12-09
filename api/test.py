from user.models import User

User.objects.load_database()

user = {'username': 'd123', 'password': 'stalkera123'}

if not User.objects.DoesNotExist(user['username']):
    print(f'Error: user with username [{user['username']}] already exists')
    exit()

valid, error = User.objects.validate(user['username'], user['password'])

if not valid:
    print(f'Error: {error}')
    exit()

User.objects.create(user['username'], user['password'])
