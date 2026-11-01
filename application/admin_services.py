from application.repositories.admin_repository import AdminRepository
from infrastructure.security.password_hasher import verify_password


class AdminService:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.admin_repository = admin_repository

    async def authenticate(self, discord_user_id, password: str) -> bool:
        admin = await self.admin_repository.get_by_discord_id(discord_user_id)
        if admin is None:
            return False
        if not admin.is_active:
            return False
        return verify_password(password, admin.password_hash)