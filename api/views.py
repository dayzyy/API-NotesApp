from aiohttp import web

async def signup(request):
    data = await request.json()
    print(data)
    return web.json_response({"email": data['email'], "password": data['password']})
