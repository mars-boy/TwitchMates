# Imports
from sanic import Sanic, Blueprint
from sanic_cors import CORS, cross_origin
from asyncpg import connect, create_pool
import os


from src.api.users.user import user_blueprint
from src.utilities.config import DB_CONFIG


app = Sanic('TwitchMates')

# Register POSTGRES 
@app.listener('before_server_start')
async def register_db(app, loop):
    app.pool = await create_pool(**DB_CONFIG, loop=loop, max_size=100)


# limiting incoming request body size to prevent out of memory in ddos
app.config.REQUEST_MAX_SIZE = 1024

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

grouped_blueprint = Blueprint.group(user_blueprint)

app.blueprint(grouped_blueprint)