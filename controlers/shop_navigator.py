import discord

from models.cart import Cart
from models.product import Product
from views.catalog_view import CatalogView
from views.product_details_view import ProductDetailsView


class ShopNavigator:
    def __init__(self, products: list[Product], cart: Cart):
        self.products = products
        self.cart = cart

    async def open_catalog(self, interaction: discord.Interaction):
        await interaction.response.edit_message(
            content="Choose a product: ",
            view=CatalogView(self)
        )

    async def open_product_details(self, interaction: discord.Interaction, product: Product):
        await interaction.response.edit_message(
            content=(
                f"Product:{product.name}\n",
                f"Price:{product.price}\n",
                f"Description:{product.description}",
            ),
            view=ProductDetailsView(self, product)
        )

    #async def open_cart(self, interaction: discord.Interaction)