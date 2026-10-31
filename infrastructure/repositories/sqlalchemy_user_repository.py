from abc import ABC, abstractmethod

from discord import User
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from infrastructure.database.connection import session_factory
from infrastructure.database.models import UserModel


class UserRepository(ABC):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory

    async def create(self, user: User) -> User:
        async with self.session_factory() as session:
            model = UserModel(
                discord_user_id = user.id
            )
            session.add(model)
            await session.commit()