import discord
from discord.ui import item

from domain.cart import Cart
from domain.product import Product
from presentation.discord.components.product_select import ProductSelect


class CartView(discord.ui.View):
    def __init__(self, navigator, cart: Cart):
        super().__init__()
        self.navigator = navigator

        if not cart.items:
            self.remove_item(self.clear_cart)
        else:
            def cart_product_description(product: Product):
                item=cart.find_item(product.id)
                return(
                    f"{item.quantity} x "
                    f"${product.price} = "
                    f"${item.total_price()}"
                )

            self.add_item(
                ProductSelect(
                    navigator=navigator,
                    products=[
                        item.product
                        for item in cart.items
                    ],
                    description=cart_product_description,
                )
            )

    @discord.ui.button(
        label="Clear cart",
        style=discord.ButtonStyle.red,
        row=4
    )
    async def clear_cart(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        self.navigator.cart_service.clear_cart(interaction.user.id)
        await self.navigator.open_cart(interaction)

    @discord.ui.button(
        label="Back to catalog",
        style=discord.ButtonStyle.blurple,
        row=4
    )
    async def back_to_catalog(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        await self.navigator.open_catalog(interaction)