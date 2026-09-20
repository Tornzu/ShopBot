import discord

from models.product import Product
from models.cart import cart

class ProductView(discord.ui.View):
    def __init__(self, product: Product):
        super().__init__()
        self.product = product

    @discord.ui.button(
        label = "Add to cart",
        style = discord.ButtonStyle.green
    )
    async def add_to_cart(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button,
    ):
        cart.append(self.product)
        await interaction.response.send_message(f"Added {self.product.name} to cart.")