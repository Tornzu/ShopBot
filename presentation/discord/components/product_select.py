from typing import Callable
import discord
from domain.product import Product


class ProductSelect(discord.ui.Select):
    def __init__(self, navigator, products: list[Product], description: Callable[[Product],str]):
        self.navigator = navigator
        options = [
            discord.SelectOption(
                label=product.name,
                description=description(product),
                value=product.id
            )
            for product in products
        ]
        super().__init__(
            placeholder="Select a product",
            options=options,
            row=0,
        )

    async def callback(self, interaction: discord.Interaction):
        product_id=int(self.values[0])
        await self.navigator.open_product_details(interaction,product_id)