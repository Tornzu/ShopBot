from discord import User

from application.repositories.user_repository import UserRepository
from infrastructure.database.base import Base


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def get_or_create(self, discord_user_id : int) -> User:
        user = await self.user_repository.get_by_discord_id(discord_user_id)
        if user:
            return user
        user = User(
            discord_user_id = discord_user_id
        )
        await self.user_repository.create(user)
        return user

