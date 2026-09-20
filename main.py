from itertools import product

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from cart import cart
from Product import Product
from views.ShopView import ShopView

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

products = [
    Product(name="Bread", price=3, description="Flat sliced white bread"),
    Product(name="Milk", price=4, description="0% fat milk"),
    Product(name="Cheese", price=2, description="dairy free cheese"),
]

basket = []

@bot.command()
async def start(ctx):
    await ctx.send("Welcome to shop market")

@bot.command()
async def shop(ctx):
    message = "Products:"
    await ctx.send(message, view=ShopView(products))

@bot.command()
async def show_cart(ctx):
    if len(cart) == 0:
        await ctx.send("Cart is empty")
        return
    message = "Your cart: \n"
    total = 0
    for product in cart:
        message += f"{product.name}: ${product.price}\n"
        total += product.price

    message += f"\nTotal: ${total}\n"
    await ctx.send(message)




bot.run(token)