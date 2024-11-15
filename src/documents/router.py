from fastapi import APIRouter, HTTPException

from .constants import RedisCacheType
from ..redis.redis import redis_client
from ..redis.service import CacheGeneratorFactory, CacheGenerator
from ..responses import DocumentResponse
from .schemas import DocumentRequest
from .service import DocumentGeneratorFactory

router = APIRouter()


@router.post("/generate")
async def generate_document(request: DocumentRequest):
    """
    Endpoint to generate a document from markdown text.
    """
    try:
        cache_generator: CacheGenerator = CacheGeneratorFactory.get_generator(RedisCacheType.DOCUMENT)
        cache_key: str = cache_generator.generate_cache_key(request.text, request.ext)

        cached_content = await redis_client.get(cache_key)
        if cached_content:
            generator = DocumentGeneratorFactory.get_generator(request.ext)
            return DocumentResponse.create(generator, cached_content)

        generator = DocumentGeneratorFactory.get_generator(request.ext)
        content = generator.generate(request.text)

        await redis_client.set(cache_key, content, expire=600)

        return DocumentResponse.create(generator, content)

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
