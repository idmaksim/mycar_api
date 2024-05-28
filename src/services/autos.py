from schemas.autos import AutoAddRequest
from utils.repository import AbstractRepository


class AutosService:
    def __init__(self, auto_repo: AbstractRepository) -> None:
        self.repo: AbstractRepository = auto_repo()

    async def get_all(self, limit: int):
        res = await self.repo.get_all(limit)
        return res

    async def add_one(self, auto: AutoAddRequest):
        auto_json = auto.model_dump()
        new_auto = await self.repo.add_one(auto_json)
        return new_auto
