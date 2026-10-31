from abc import ABC, abstractmethod

from discord import User


class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        pass
