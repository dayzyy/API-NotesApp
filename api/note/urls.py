from aiohttp import web
from note.views import add, get_notes

urls = [
    web.post('/notes/add', add),
    web.get('/notes', get_notes)
]
