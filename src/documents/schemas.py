from pydantic import BaseModel, Field

from src.documents.constants import FileExtension


class DocumentRequest(BaseModel):
    text: str = Field(..., description="Markdown text to convert")
    ext: FileExtension = Field(..., description="File extension (pdf, docx or txt)")
