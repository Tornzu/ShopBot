import discord

from models.product import Product
from models.cart import cart
from views.cart_view import ViewCart

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
        await interaction.response.edit_message(view=None)
        await interaction.followup.send(f"Product: {self.product.name}\nWas added to cart sucessfully.", view=ViewCart())

