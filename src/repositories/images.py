from db.models.images import Images
from utils.repository import SQLAlchemyRepository


class ImagesRepository(SQLAlchemyRepository):
    model = Images
