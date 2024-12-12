import argparse

from context.notecontext import add

parser = argparse.ArgumentParser(description='Manage your notes')

note_subparser = parser.add_subparsers(dest='command', help='available commands')

add_parser = note_subparser.add_parser('add', help='create a note')
add_parser.add_argument('body', help='Content of the note')

args = parser.parse_args()

match args.command:
    case 'add':
        add(args.body)
