from db.models.images import Images
from utils.repository import AbstractRepository


class ImagesService:
    def __init__(self, image_repo: AbstractRepository) -> None:
        self.repo: AbstractRepository = image_repo()

    async def get_image_path_by_id(self, image_id: int):
        image: Images = await self.repo.get_one_by_id(image_id)
        if image is None:
            raise Exception("Image not found")
        image_name: str = image.filename
        return '../images/' + image_name + '.jpg'