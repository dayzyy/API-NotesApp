from aiohttp import web
from urls import urls
from user.models import User
from note.models import Note

app = web.Application()
app.add_routes(urls)

if __name__ == '__main__':
    User.objects.load_database()
    Note.objects.load_database()

    print('\nAvailable endpoints: [', end='\n\n')
    for route in urls:
        print(f'    {route.path}')
    print('\n] ola :p', end='\n\n')

    web.run_app(app)
