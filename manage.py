import argparse

from api.tokens.models import Token, IsAuthenticated
from api.user.models import User
from context.authcontext import register, login, load_storage, saved_token

load_storage()
User.objects.load_database()

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest='command', help='available commands')

register_parser = subparser.add_parser('register')
register_parser.add_argument('username', help='your username')
register_parser.add_argument('password', help='your password')

login_parser = subparser.add_parser('login')
login_parser.add_argument('username', help='your username')
login_parser.add_argument('password', help='your password')

args = parser.parse_args()

match args.command:
    case 'register':
        print(f'registering with {args.username}, {args.password}')
        register(args.username, args.password)

    case 'login':
        print(f'loging in with {args.username}, {args.password}')
        login(args.username, args.password)
