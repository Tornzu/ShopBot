from abc import ABC, abstractmethod

from domain.admin import Admin


class AdminRepository(ABC):
    @abstractmethod
    async def get_by_discord_id(self, discord_user_id: int) -> Admin | None:
        pass

    @abstractmethod
    async def create(self, discord_user_id: int, password_hash: str) -> Admin | None:
        pass