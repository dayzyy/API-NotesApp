import argparse

from context.notecontext import add, get_notes

parser = argparse.ArgumentParser(description='Manage your notes')

subparser = parser.add_subparsers(dest='command', help='available commands')

add_parser = subparser.add_parser('add', help='create a note')
add_parser.add_argument('body', help='Content of the note')

list_parser = subparser.add_parser('list', help='list your notes. You can filter them by status')
list_parser.add_argument('--filter', '-f', choices=['todo', 'in-progress', 'done'], help='filter for the notes', required=False)

args = parser.parse_args()

match args.command:
    case 'add':
        add(args.body)

    case 'list':
        get_notes(args.filter)
