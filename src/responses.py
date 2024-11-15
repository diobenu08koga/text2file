from fastapi.responses import StreamingResponse
from io import BytesIO
from src.documents.service import DocumentGenerator

class DocumentResponse:
    @staticmethod
    def create(generator: DocumentGenerator, content: bytes) -> StreamingResponse:
        """
        Create a streaming response from the document generator and content.
        """
        filename = f"document.{generator.filename_extension}"
        media_type = generator.media_type

        file_stream = BytesIO(content)
        file_stream.seek(0)

        response = StreamingResponse(
            file_stream,
            media_type=media_type,
            headers={
                "Content-Disposition": f'attachment; filename="{filename}"'
            }
        )

        return response