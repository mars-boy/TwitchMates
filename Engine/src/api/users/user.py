# Imports
from sanic import Blueprint, response
import asyncio
import aiohttp
from functools import wraps

from src.utilities.requestutility import httpget

import src.repository.user as user_repo
from src.utilities.config import DB_CONFIG


# Config
user_blueprint = Blueprint(
    'user_blueprint',url_prefix='/api/users'
)

#Routes
@user_blueprint.route('/checkauthtoken/<idtoken>', methods=['GET'])
async def checkauthtoken(request, idtoken: str):
    HEADERS = {
        'Authorization' : 'Bearer ' +idtoken,
        'Client-ID': 'n457nns10qv4jnkr33seiaqkh299kb'
    }
    user_response = await httpget( 'https://api.twitch.tv/helix/users', HEADERS )
    if(user_response['status'] == 200):
        resp = await user_repo.checkuserifexist(request.app, user_response)
        if(resp):
            return response.json(
            user_response,
            status=200
        )
        else:
            resp = await user_repo.createuser(request.app, user_response)
            if(resp):
                return response.json({
                    'data':'completed',
                    'status': 200
                }, status=200)
            else:
                return response.json({
                    'data':'try again',
                    'status': 400
                }, status=200)
    else:
        return response.json( { 
            'data': 'Please contact admin',
            'status': 500
        }, status = 200)


