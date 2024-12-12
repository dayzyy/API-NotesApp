from aiohttp import web
import json
import base64

from tokens.models import IsAuthenticated
from note.models import Note

async def add(request):
    data = await request.json()
    token = request.headers.get('Authorization')

    if not IsAuthenticated(token):
        return web.json_response(status=401)

    encoded_payload, _ = token.split('.')

    payload = base64.urlsafe_b64decode(encoded_payload).decode()
    json_payload = json.loads(payload)

    Note.objects.create(json_payload['username'], data['body'])

    if len(data['body']) <= 25:
        note_preview = data['body']
    else:
        note_preview = f'{data['body'][:25]}...'

    return web.json_response(text=f'Note succesfully created: "{note_preview}"', status=200)
