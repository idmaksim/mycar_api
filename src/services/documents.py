from db.models.documents import Documents
from db.models.users import Users
from schemas.documents import DocumentAddRequest
from utils.repository import AbstractRepository


class DocumentsService:
    def __init__(self, document_repo: AbstractRepository, user_repo: AbstractRepository) -> None:
        self.docs_repo: AbstractRepository = document_repo()
        self.user_repo: AbstractRepository = user_repo()
    
    async def get_all(self, limit):
        documents = await self.docs_repo.get_all(limit)
        return documents

    async def add_document(self, document: DocumentAddRequest):
        doc_dict = document.model_dump()
        new_doc: Documents = await self.docs_repo.add_one(doc_dict)
        return new_doc

    async def get_by_user_email(self, user_email: str):
        user: Users = await self.user_repo.get_one_by_data(email=user_email)
        print(user)
        if user:
            document: Documents = await self.docs_repo.get_one_by_id(user.id)
            return document
        raise Exception('user with this email doesn\'t found')
    
    async def update_by_id(self, id: int, document: DocumentAddRequest):
        doc_dict = document.model_dump()
        doc: Documents = await self.docs_repo.update_one_by_id(id, doc_dict)
        return doc

