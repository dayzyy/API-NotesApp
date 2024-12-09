from aiohttp import web
from views import register

urls = [
    web.post('/register', register)
]
