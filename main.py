import asyncio
import sys
import discord
from discord.ext import commands
from application.admin_services import AdminService
from application.admin_session_service import AdminSessionService
from application.cart_service import CartService
from application.product_service import ProductService
from application.user_services import UserService
from config.settings import DISCORD_TOKEN
from infrastructure.database.connection import session_factory
from infrastructure.repositories.sqlalchemy_admin_repository import SqlAlchemyAdminRepository
from infrastructure.repositories.sqlalchemy_cart_repository import SqlAlchemyCartRepository
from infrastructure.repositories.sqlalchemy_product_repository import SqlAlchemyProductRepository
from infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from presentation.discord.admin.admin_login_view import AdminLoginView
from presentation.discord.shop_navigator import ShopNavigator
from presentation.discord.views.catalog_view import CatalogView

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

product_repository = SqlAlchemyProductRepository(session_factory)
cart_repository = SqlAlchemyCartRepository(session_factory)
user_repository = SqlAlchemyUserRepository(session_factory)
admin_repository = SqlAlchemyAdminRepository(session_factory)

user_service = UserService(user_repository)
product_service = ProductService(product_repository)
cart_service = CartService(
    cart_repository = cart_repository,
    user_service = user_service,
    product_service = product_service,
)
admin_service = AdminService(admin_repository)
admin_session_service = AdminSessionService()

navigator = ShopNavigator(
    cart_service=cart_service,
    product_service=product_service,
)

@bot.command()
async def start(ctx):
    await user_service.get_or_create(ctx.author.id)
    await ctx.send("Welcome to shop market")

@bot.command()
async def shop(ctx):
    message = "Choose a product:"
    await ctx.send(message, view=CatalogView(navigator, products= await product_service.get_all_products()))

@bot.command()
async def clear(ctx):
    async for message in ctx.channel.history():
        await message.delete()

@bot.command()
async def admin(ctx):
    admin_user = await admin_repository.get_by_discord_id(ctx.author.id)
    if admin_user is None or not admin_user.is_active:
        await ctx.send("Access denied")
        return
    await ctx.send(
        "Admin login",
        view = AdminLoginView(
            admin_service = admin_service,
            admin_session_service = admin_session_service,
            user_id = admin_user.id,
        )
    )
bot.run(DISCORD_TOKEN)