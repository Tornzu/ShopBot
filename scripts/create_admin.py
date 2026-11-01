import asyncio
import sys
from getpass import getpass

from infrastructure.database.connection import session_factory
from infrastructure.repositories.sqlalchemy_admin_repository import SqlAlchemyAdminRepository
from infrastructure.security.password_hasher import hash_password


async def main():
    repository = SqlAlchemyAdminRepository(session_factory)
    discord_user_id = int(input("Enter discord user id: "))
    password = getpass("Enter password: ")

    if not password:
        print("Password is required")
        return
    existing_admin = await repository.get_by_discord_id(discord_user_id)
    if existing_admin:
        print("Admin already exists")
        return
    password_hash = hash_password(password)
    await repository.create(discord_user_id, password_hash)
    print("Admin created")

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())