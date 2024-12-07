from aiohttp import web
from views import signup

urls = [
    web.post('/signup', signup)
]
