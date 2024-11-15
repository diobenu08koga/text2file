from fastapi import FastAPI

from src.documents.router import router as documents_router
from src.redis.redis import redis_client

app = FastAPI()

# Starting connection with Redis
@app.on_event("startup")
async def startup_event():
    await redis_client.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await redis_client.close()

app.include_router(documents_router, prefix="/documents")
