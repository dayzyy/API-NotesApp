from aiohttp import web
from views import is_authenticated, register, login

urls = [
    web.post('/register', register),
    web.post('/login', login),
    web.get('/status', is_authenticated),
]
