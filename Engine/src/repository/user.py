import json
from collections import namedtuple


from src.utilities.requestutility import DeserialisedObj
from src.models.Users import Users

async def checkuserifexist(app, user_response):
    userid = user_response['data']['data'][0]['id']
    async with app.pool.acquire() as connection:
        sql = f'SELECT * FROM USERS WHERE ID = {userid}'
        results = await connection.fetch(sql)
    return len(results) > 0


async def createuser(app, user_response):
    userobj = user_response['data']['data'][0]
    obj = namedtuple('Users', userobj.keys())(*userobj.values())
    # obj = DeserialisedObj(json.dumps(user_response['data']['data'][0]))
    sql = f""" INSERT INTO USERS (id, login, display_name, email, active) 
        VALUES ({ obj.id }, '{ obj.login }', '{ obj.display_name }', '{ obj.email }', True)
        """
    async with app.pool.acquire() as connection:
        await connection.execute(sql)
    return True