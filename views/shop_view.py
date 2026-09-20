import discord

from views.product_view import ProductView


class ShopView(discord.ui.View):
    def __init__(self, products):
        super().__init__()
        for product in products:
            button = discord.ui.Button(
                label=product.name,
                style=discord.ButtonStyle.green
            )
            button.callback = self.create_callback(product)
            self.add_item(button)

    def create_callback(self, product):
        async def callback(interaction: discord.Interaction):
            await interaction.response.send_message(f"{product.name}: ${product.price},{product.description}", view=ProductView(product))

        return callback