from enum import Enum


class FileExtension(str, Enum):
    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"

class RedisCacheType(str, Enum):
    DOCUMENT = "document"