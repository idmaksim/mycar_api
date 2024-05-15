from db.models.documents import Documents
from schemas.documents import DocumentAddRequest
from utils.repository import AbstractRepository


class DocumentsService:
    def __init__(self, document_repo: AbstractRepository) -> None:
        self.docs_repo: AbstractRepository = document_repo()

    async def add_document(self, document: DocumentAddRequest):
        doc_dict = document.model_dump()
        new_doc: Documents = await self.docs_repo.add_one(doc_dict)
        return new_doc

    