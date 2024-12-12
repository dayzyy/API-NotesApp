import argparse

from context.authcontext import register, login, logout, status, load_storage

load_storage()

parser = argparse.ArgumentParser(description='Authentication')

subparser = parser.add_subparsers(dest='command', help='available commands')

register_parser = subparser.add_parser('register')
register_parser.add_argument('username', help='your username')
register_parser.add_argument('password', help='your password')

login_parser = subparser.add_parser('login')
login_parser.add_argument('username', help='your username')
login_parser.add_argument('password', help='your password')

logout_parser = subparser.add_parser('logout')

status_parser = subparser.add_parser('status', help='see your authorization status')


args = parser.parse_args()

match args.command:
    case 'register':
        print(f'registering with [{args.username} {args.password}]')
        register(args.username, args.password)

    case 'login':
        print(f'loging in with [{args.username} {args.password}]')
        login(args.username, args.password)

    case 'logout':
        print(f'Logging out...')
        logout()

    case 'status':
        print(f'Authorization status...')
        status()
