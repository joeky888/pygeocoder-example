from aiohttp import web
import geocoder

async def handleip(request):
    peername = request.transport.get_extra_info('peername')
    host = ""
    if peername is not None:
        host, port = peername
    if host == "" or host == "127.0.0.1" or host == "0.0.0.0":
        host = "me"
    print(host)
    latlng = geocoder.ip(host).latlng
    if latlng:
        iptext = '{' \
                 '"lat":'      + str(latlng[0]) +\
                 ',"lng":'      + str(latlng[1]) +\
                 '}'
    else:
        iptext = '{}'
    return web.Response(text=iptext)


app = web.Application()
app.add_routes([web.get('/ip', handleip)])

web.run_app(app, port=1919)
