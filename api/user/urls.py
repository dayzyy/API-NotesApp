from aiohttp import web
from user.views import is_authenticated, register, login

urls = [
    web.post('/users/register', register),
    web.post('/users/login', login),
    web.get('/users/status', is_authenticated)
]
