from db.models.autos import Autos
from utils.repository import SQLAlchemyRepository


class AutosRepository(SQLAlchemyRepository):
    model = Autos