from typing import Any
import redis.asyncio as redis

import os

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

class RedisClient:
    def __init__(self):
        self.redis = None

    async def connect(self):
        self.redis = await redis.from_url(REDIS_URL)

    async def close(self):
        await self.redis.close()

    async def get(self, key: str) -> Any:
        return await self.redis.get(key)

    async def set(self, key: str, value: str, expire: int = None):
        await self.redis.set(key, value, ex=expire)

redis_client = RedisClient()
