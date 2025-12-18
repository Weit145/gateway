from fastapi import Request

from app.core.redis.rd_hellper import rd_helper


class RedisRepository:
    async def rate_limit(self, request: Request):
        ip = request.client.host
        limit_conf = await rd_helper.get_limit(request)
        if not limit_conf:
            return True

        limit, window = limit_conf
        key = f"rate:{request.method}:{request.url.path}:{ip}"

        try:
            is_new = await rd_helper.client.set(key, 1, ex=window, nx=True)
            if not is_new:
                count = await rd_helper.client.incr(key)
            else:
                count = 1
            if count > limit:
                return False
            return True
        except Exception as e:
            print(f"Redis error in rate limit: {e}", flush=True)
            return True
