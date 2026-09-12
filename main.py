import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        await bot.process_commands(message)
        await message.channel.send(message.content)

@bot.command()
async def button(ctx):

    view = discord.ui.View()

    async def button_callback(interaction: discord.Interaction):
        await interaction.response.send_message("You clicked the button")

    button = discord.ui.Button(
        label="Click me",
        style=discord.ButtonStyle.blurple,
    )

    button.callback = button_callback
    view.add_item(button)


    await ctx.send("Click the button", view=view)

bot.run(token)