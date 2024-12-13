from aiohttp import web
import json
import base64

from tokens.models import IsAuthenticated
from note.models import Note
from user.models import User

def authenticate(token):
    if not IsAuthenticated(token):
        return None

    encoded_payload, _ = token.split('.')

    payload = base64.urlsafe_b64decode(encoded_payload).decode()
    json_payload = json.loads(payload)
    
    return User.objects.get(json_payload['username'])

async def add(request):
    data = await request.json()
    token = request.headers.get('Authorization')

    user = authenticate(token)
    if user is None:
        return web.json_response(status=401)

    Note.objects.create(user.username, data['body'])

    if len(data['body']) <= 25:
        note_preview = data['body']
    else:
        note_preview = f'{data['body'][:25]}...'

    return web.json_response(text=f'Note succesfully created: "{note_preview}"', status=200)

async def get_notes(request):
    token = request.headers.get('Authorization')

    user = authenticate(token)
    if user is None:
        return web.json_response(status=401)

    data = await request.json()

    notes = Note.objects.filter(username=user.username, status=data['filter'])

    data = json.dumps(notes)

    return web.json_response(data, status=200)

async def remove(request):
    token = request.headers.get('Authorization')

    user = authenticate(token)
    if user is None:
        return web.json_response(status=401)

    data = await request.json()

    if Note.objects.DoesNotExist(user.username, int(data['id'])):
        return web.json_response(status=404)

    Note.objects.remove(user.username, data['id'])
    return web.json_response(status=200)
