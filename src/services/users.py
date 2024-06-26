from db.models.users import Users
from schemas.users import UserAddRequest
from utils.repository import AbstractRepository


class UsersService:
    def __init__(self, user_repo: AbstractRepository) -> None:
        self.users_repo: AbstractRepository = user_repo()

    async def add_user(self, user: UserAddRequest):
        user_dict = user.model_dump()
        new_user: Users = await self.users_repo.add_one(user_dict)
        new_user.__delattr__('password')
        return new_user

    async def get_one(self, email: str, password: str):
        user: Users = await self.users_repo.get_one_by_data(email=email, password=password)
        if user:
            user.__delattr__('password')
        return user
