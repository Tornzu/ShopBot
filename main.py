import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from Product import Product

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

products = [
    Product(name="Bread", price="$3", description="Flat sliced white bread"),
    Product(name="Milk", price="$2", description="0% fat milk"),
    Product(name="Cheese", price="$4", description="dairy free cheese"),
]

basket = []

@bot.command()
async def start(ctx):
    await ctx.send("Welcome to shop market")



@bot.command()
async def shop(ctx):
    message = ""
    view = discord.ui.View()
    for product in products:
        async def callback(interaction: discord.Interaction, product=product):
            await interaction.response.send_message(f"{product.name}: {product.price},{product.description}",
                                                    view=view2)

        async def addbasket_callback(interaction: discord.Interaction, product=product):
            basket.append(product)
            await interaction.response.send_message(f"Product {product.name} added to basket")

        message += f"{product.name}: {product.price}\n"

        button1 = discord.ui.Button(
            label=product.name,
            style=discord.ButtonStyle.green
        )

        view2 = discord.ui.View()

        addBasketButton = discord.ui.Button(
            label="add to basket",
            style=discord.ButtonStyle.green
        )
        addBasketButton.callback = addbasket_callback
        view2.add_item(addBasketButton)


        button1.callback = callback
        view.add_item(button1)

    message += "Select a product: "

    await ctx.send(message, view=view)





bot.run(token)