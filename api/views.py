from aiohttp import web
from user.models import User

async def register(request):
    data = await request.json()

    print(data)
    
    if not User.objects.DoesNotExist(data['username']):
        return web.json_response(text=f'user with username ({data['username']}) already exists!', status=409)

    valid, error = User.objects.validate(**data)

    if not valid:
        return web.json_response(text=error, status=422)

    User.objects.create(**data)

    return web.json_response(text='Successful registration!', status=200)
