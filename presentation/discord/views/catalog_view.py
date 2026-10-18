import discord

from domain.product import Product
from presentation.discord.components.product_select import ProductSelect


class CatalogView(discord.ui.View):
    def __init__(self, navigator, products: list[Product]):
        super().__init__()
        self.navigator = navigator
        self.add_item(
            ProductSelect(
                navigator=navigator,
                products=products,
                description=lambda product: (
                    f"{product.description} - ${product.price}"
                ),
            )
        )

    @discord.ui.button(
        label="View cart",
        style=discord.ButtonStyle.blurple,
        row=1
    )
    async def show_cart(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        await self.navigator.open_cart(interaction)
