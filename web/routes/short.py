__all__ = ('setup_routes',)
import random

from sanic.response import json

from config import Settings
from schemas import Link


def setup_routes(app):
    @app.post('/shorten')
    async def create_link(request):
        data = request.json
        link_obj = Link(**data)
        chars = 'asdfghjklqwertyuiopzxcvbnm1234567890'
        short_id = ''.join(random.choices(chars, k=7))
        short_url = f'http://bestofthebest/{short_id}'
        redis = Settings.get_redis
        redis.set(short_id, link_obj.link)
        return json(
            {'status': 'success', 'short_url': short_url, 'id': short_id},
            status=201,
        )

    @app.get('/long/<short_id:str>')
    async def get_link(request, short_id: str):
        redis = Settings.get_redis
        raw_link = redis.get(short_id)

        if raw_link is None:
            return json(
                {
                    'status': 'error',
                    'message': 'Ссылка не найдена или устарела',
                },
                status=404,
            )
        link = raw_link.decode('utf-8')

        return json(
            {
                'status': 'success',
                'link': link,
            },
            status=200,
        )
