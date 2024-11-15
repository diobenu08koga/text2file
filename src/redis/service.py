from abc import ABC, abstractmethod
from typing import Any

from src.documents.constants import RedisCacheType


class CacheGenerator(ABC):
    """
    Abstract base class for generating cache keys.
    """

    @staticmethod
    @abstractmethod
    def generate_cache_key(obj: str, *args: Any, **kwargs: Any) -> str:
        """
        Generates cache key.
        """
        pass

    @property
    @abstractmethod
    def cache_type(self) -> str:
        """
        Returns the cache type for the corresponding cache generator
        """
        pass


class DocumentCacheGenerator(CacheGenerator):
    """
    Class for generating cache keys for the documents
    """

    @property
    def cache_type(self) -> str:
        return RedisCacheType.DOCUMENT.value

    @staticmethod
    def generate_cache_key(obj: str, *args: Any, **kwargs: Any) -> str:
        """
        Generates cache key for the document.
        """
        ext = kwargs.get("ext", "txt")
        additional_identifiers = ":".join(str(arg) for arg in args)

        return f"document_cache:{ext}:{hash(obj)}:{additional_identifiers}"


class CacheGeneratorFactory:
    """
    Factory class to return the appropriate cache generator.
    """

    # Mapping cache types to their corresponding generator classes
    _generators = {
        RedisCacheType.DOCUMENT: DocumentCacheGenerator,
    }

    @staticmethod
    def get_generator(cache_type: RedisCacheType) -> CacheGenerator:
        generator_class = CacheGeneratorFactory._generators.get(cache_type)
        if not generator_class:
            raise ValueError(f"No cache generator found for type: {cache_type}")
        return generator_class()
