from abc import ABC, abstractmethod

from domain.user import User


class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def get_by_discord_id(self, discord_user_id: int) -> User | None:
        pass
