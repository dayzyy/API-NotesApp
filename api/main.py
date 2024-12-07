from aiohttp import web
from urls import urls

app = web.Application()
app.add_routes(urls)

if __name__ == '__main__':
    web.run_app(app)
