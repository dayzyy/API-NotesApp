from user.urls import urls as user_urls
from note.urls import urls as note_urls

urls = [
    *user_urls,
    *note_urls,
]
