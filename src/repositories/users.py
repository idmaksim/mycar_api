from db.models.users import Users
from db.models.documents import Documents
from utils.repository import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = Users


class DocumentsRepository(SQLAlchemyRepository):
    model = Documents
