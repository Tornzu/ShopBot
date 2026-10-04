import discord

from models.cart import Cart
from models.product import Product


class ProductDetailsView(discord.ui.View):
    def __init__(self, navigator, product: Product):
        super().__init__()
        self.navigator = navigator
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
        self.navigator.cart.add_product(self.product)
        await interaction.response.edit_message(
            content = f"Product {self.product.name} added to cart.",
            view=self
        )
    @discord.ui.button(
        label = "Back to catalog",
        style = discord.ButtonStyle.red
    )
    async def back_to_catalog(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button,
    ):
        await self.navigator.open_catalog(interaction)