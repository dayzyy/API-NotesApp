from aiohttp import web
from views import register, login

urls = [
    web.post('/register', register),
    web.post('/login', login),
]
