from sanic import Sanic
from sanic.response import json
import aiohttp

app = Sanic()


async def ip(iip):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://ip-api.com/json/'+iip, timeout=6) as resp:
            print(resp.status)
            return (await resp.text()).encode('utf-8')



@app.route("/")
async def test(request):
    print (request.ip)
    print ('--------')
    try:
        r = await ip(request.ip[0])
    except:
        r = 'timeout'
    return json(r)
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


