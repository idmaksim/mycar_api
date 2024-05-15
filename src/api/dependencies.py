from repositories.documents import DocumentsRepository
from repositories.users import UsersRepository
from services.documents import DocumentsService
from services.users import UsersService


def users_service():
    return UsersService(UsersRepository)


def documents_service():
    return DocumentsService(DocumentsRepository)
