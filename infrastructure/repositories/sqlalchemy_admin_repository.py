from cffi import model
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from application.repositories.admin_repository import AdminRepository
from domain.admin import Admin
from infrastructure.database.models import UserModel, AdminModel


class SqlAlchemyAdminRepository(AdminRepository):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory

    async def get_by_discord_id(self, discord_user_id: int) -> Admin | None:
        async with self.session_factory() as session:
            result = await session.execute(
                select(AdminModel)
                .where(AdminModel.discord_user_id == discord_user_id)
            )

            model = result.scalar_one_or_none()
            if model is None:
                return None
            return self._to_domain(model)

    async def create(self, discord_user_id: int, password_hash: str) -> Admin | None:
        async with self.session_factory() as session:
            model = AdminModel(
                discord_user_id=discord_user_id,
                password_hash=password_hash,
            )

            session.add(model)
            await session.commit()

    def _to_domain(self, model: AdminModel) -> Admin:
        return Admin(
            id = model.discord_user_id,
            discord_user_id = model.discord_user_id,
            password_hash=model.password_hash,
            is_active=model.is_active,
            created_at=model.created_at,
            )
