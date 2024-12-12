import argparse

parser = argparse.ArgumentParser(description='Manage your notes')

note_subparser = parser.add_subparsers(dest='command', help='available commands')

add_parser = note_subparser.add_parser('add', help='create a note')

args = parser.parse_args()
