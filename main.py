import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from models.cart import cart
from models.product_list import products
from views.shop_view import ShopView
from views.cart_view import ViewCart
from views.cart_item_remove_view import RemoveProductView

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def start(ctx):
    await ctx.send("Welcome to shop market")

@bot.command()
async def shop(ctx):
    message = "Products:"
    await ctx.send(message, view=ShopView(products))
    await ctx.message.delete()

@bot.command()
async def cart(ctx):
    message = "Do you wish to view your cart?"
    await ctx.send(message, view=ViewCart())

@bot.command()
async def remove(ctx):
    message = "Which item would you like to remove from your cart?"
    await ctx.send(message, view=RemoveProductView())

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