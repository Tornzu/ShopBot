from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from application.repositories.user_repository import UserRepository
from domain.user import User
from infrastructure.database.models import UserModel


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory

    async def create(self, user: User) -> None:
        async with self.session_factory() as session:
            model = UserModel(
                discord_user_id = user.discord_user_id
            )
            session.add(model)
            await session.commit()

    async def get_by_discord_id(self, discord_user_id: int) -> User | None:
        async with self.session_factory() as session:
            result = await session.execute(
                select(UserModel).where(UserModel.discord_user_id == discord_user_id)
            )
            model = result.scalar_one_or_none()
            if model is None:
                return

            return self.to_domain(model)

    @staticmethod
    def to_domain(model: UserModel) -> User:
        return User(
            discord_user_id = model.discord_user_id,
            id = model.id
        )