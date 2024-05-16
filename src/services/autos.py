from db.models.autos import Autos
from utils.repository import AbstractRepository


class AutosService:
    def __init__(self, auto_repo: AbstractRepository) -> None:
        self.repo: AbstractRepository = auto_repo()

    async def get_all(self, limit: int):
        res = await self.repo.get_all(limit)
        return res

    