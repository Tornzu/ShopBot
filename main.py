import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from controlers.shop_navigator import ShopNavigator
from models.cart import Cart
from models.product_list import products
from views.catalog_view import CatalogView

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
cart = Cart()
navigator = ShopNavigator(
    products=products,
    cart=cart,
)

@bot.command()
async def start(ctx):
    await ctx.send("Welcome to shop market")

@bot.command()
async def shop(ctx):
    message = "Choose a product:"
    await ctx.send(message, view=CatalogView(navigator))

@bot.command()
async def clear(ctx):
    async for message in ctx.channel.history():
        await message.delete()

bot.run(token)