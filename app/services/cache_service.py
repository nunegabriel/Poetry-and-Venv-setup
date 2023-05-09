import redis
from functools import wraps


def cache():
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{args}:{kwargs}"
            redis_client = redis.Redis(host='localhost', port=6379, db=0)
            cached_result = redis_client.get(cache_key)
            if cached_result:
                return cached_result
            result = await func(*args, **kwargs)
            redis_client.set(cache_key, result)
            return result

        return wrapper

    return decorator
