import argparse

from context.notecontext import add, get_notes, delete

parser = argparse.ArgumentParser(description='Manage your notes')

subparser = parser.add_subparsers(dest='command', help='available commands')

add_parser = subparser.add_parser('add', help='create a note')
add_parser.add_argument('body', help='Content of the note')

list_parser = subparser.add_parser('list', help='list your notes. You can filter them by status')
list_parser.add_argument('--filter', '-f', choices=['todo', 'in-progress', 'done'], help='filter for the notes', required=False)

delete_parser = subparser.add_parser('delete', help='delete a note')
delete_parser.add_argument('id', type=int, help='id of the note to delete')

args = parser.parse_args()

match args.command:
    case 'add':
        add(args.body)

    case 'list':
        get_notes(args.filter)

    case 'delete':
        delete(args.id)
