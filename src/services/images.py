from utils.repository import AbstractRepository


class AutosService:
    def __init__(self, image_repo: AbstractRepository) -> None:
        self.repo: AbstractRepository = image_repo()

    def get_image_by_id(image_id: int):
        pass