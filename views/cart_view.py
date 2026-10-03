import discord
from models.cart import cart
from views.cart_item_remove_view import RemoveProductView

class ViewCart(discord.ui.View):
    def __init__(self):
        super().__init__()
        button = discord.ui.Button(
            label="View cart",
            style=discord.ButtonStyle.green
        )
        button.callback = self.create_callback()
        self.add_item(button)


    def create_callback(self):
        async def callback(interaction: discord.Interaction):
            message = ""
            total = 0
            if len(cart) == 0:
                message += "Empty"
            else:
                for product in cart:
                    message += f"{product.name}: ${product.price}\n"
                    total = total + product.price
            await interaction.response.edit_message(view=None)
            await interaction.followup.send(f"Cart:\n{message}\nTotal: ${total}\n", view=RemoveProductView())

        return callback

