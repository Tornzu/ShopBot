import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from application.cart_service import CartService
from application.product_service import ProductService
from domain.product import Product
from infrastructure.repositories.in_memory_cart_repository import InMemoryCartRepository
from infrastructure.repositories.in_memory_product_repository import InMemoryProductRepository
from presentation.discord.shop_navigator import ShopNavigator
from presentation.discord.views.catalog_view import CatalogView

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

products = [
    Product(id=1, name="Bread", price=3, description="Flat sliced white bread"),
    Product(id=2, name="Milk", price=4, description="0% fat milk"),
    Product(id=3, name="Cheese", price=2, description="dairy free cheese"),
]

product_repository = InMemoryProductRepository(products)

cart_repository = InMemoryCartRepository()

product_service = ProductService(product_repository)

cart_service = CartService(cart_repository, product_repository)


navigator = ShopNavigator(
    cart_service=cart_service,
    product_service=product_service,
)

@bot.command()
async def start(ctx):
    await ctx.send("Welcome to shop market")

@bot.command()
async def shop(ctx):
    message = "Choose a product:"
    await ctx.send(message, view=CatalogView(navigator, products=product_service.get_all_products()))

@bot.command()
async def clear(ctx):
    async for message in ctx.channel.history():
        await message.delete()

bot.run(token)