from aiohttp import web
from note.views import add

urls = [
    web.post('/notes/add', add)
]
