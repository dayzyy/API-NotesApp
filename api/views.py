from aiohttp import web
from user.models import User
from tokens.models import Token

async def register(request):
    data = await request.json()

    if not User.objects.DoesNotExist(data['username']):
        return web.json_response(text=f'user with username ({data['username']}) already exists!', status=409)

    valid, error = User.objects.validate(**data)

    if not valid:
        return web.json_response(text=error, status=422)

    User.objects.create(**data)

    return web.json_response(text='Successful registration!', status=200)

async def login(request):
    data = await request.json()

    users = User.objects.all()

    for user in users:
        if user.username == data['username'] and user.password == data['password']:
            token = Token.issue(user.id, user.username)

            data = {
                "text": "Successful login!",
                "token": token
            }

            return web.json_response(data, status=200)

    return web.json_response(text='Wrong credentials!', status=401)
