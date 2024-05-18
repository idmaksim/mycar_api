from db.models.documents import Documents
from utils.repository import SQLAlchemyRepository


class DocumentsRepository(SQLAlchemyRepository):
    model = Documents
