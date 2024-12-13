from aiohttp import web
from note.views import add, get_notes, remove, update

urls = [
    web.post('/notes/add', add),
    web.get('/notes', get_notes),
    web.post('/notes/remove', remove),
    web.post('/notes/update', update)
]
