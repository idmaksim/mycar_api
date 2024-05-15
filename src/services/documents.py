from utils.repository import AbstractRepository


class UsersService:
    def __init__(self, user_repo: AbstractRepository) -> None:
        self.users_repo: AbstractRepository = user_repo()