from redis.asyncio import Redis
from fastapi import Request
from ..config import settings


class RedisHellper:
    def __init__(
        self,
        url: str,
        decode_responses: bool = True,
        post: int = 5,
        get: int = 300,
        put: int = 5,
        delete: int = 5,
        time: int = 60,
    ):
        self.client = Redis.from_url(url=url, decode_responses=decode_responses)
        self.post = post
        self.get = get
        self.put = put
        self.delete = delete
        self.time = time

    async def get_limit(self, request: Request):
        if request.method == "POST":
            return (self.post, self.time)
        elif request.method == "GET":
            return (self.get, self.time)
        elif request.method == "PUT":
            return (self.put, self.time)
        elif request.method == "DELETE":
            return (self.delete, self.time)
        else:
            return None


rd_helper = RedisHellper(url=settings.redis_url)
