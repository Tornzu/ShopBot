import discord
from models.cart import cart

class RemoveProductView(discord.ui.View):
    def __init__(self):
        super().__init__()
        for product in cart:
            button = discord.ui.Button(
                label=f"Remove {product.name}?",
                style=discord.ButtonStyle.green
            )
            button.callback = self.create_callback(product)
            self.add_item(button)

    def create_callback(self, product):
        async def callback(interaction: discord.Interaction):
            cart.remove(product)
            await interaction.response.edit_message(view=None)
            await interaction.followup.send(f"{product.name} has been removed from your cart.")

        return callback