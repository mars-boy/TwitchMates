import aiohttp
import json

async def httpget(url: str, header: dict = {} , params:dict ={}):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header, params = params) as resp:
            result = { 
                'data': await resp.json(),
                'status': resp.status
            }
    return result



# Utilities

class DeserialisedObj(object):
    def __init__(self, jsonobj):
        self.__dict__ = json.loads(jsonobj)