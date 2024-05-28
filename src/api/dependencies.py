from repositories.autos import AutosRepository
from repositories.documents import DocumentsRepository
from repositories.images import ImagesRepository
from repositories.users import UsersRepository
from services.autos import AutosService
from services.documents import DocumentsService
from services.users import UsersService


def users_service():
    return UsersService(UsersRepository)


def documents_service():
    return DocumentsService(DocumentsRepository, UsersRepository)


def autos_service():
    return AutosService(AutosRepository)


def images_service():
    return images_service(ImagesRepository)
