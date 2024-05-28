from db.models.images import Images
from utils.repository import AbstractRepository


class ImagesService:
    def __init__(self, image_repo: AbstractRepository) -> None:
        self.repo: AbstractRepository = image_repo()

    async def get_image_name_by_id(self, image_id: int):
        image: Images = await self.repo.get_one_by_id(image_id)
        image_name: str = image.name
        return image_name