import discord

from models.cart import Cart


class CartView(discord.ui.View):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator

        if not navigator.cart.products:
            self.remove_item(self.clear_cart)

        for product in self.navigator.cart.products:
            remove_button = discord.ui.Button(
                label=f"❌ {product.name}",
                style=discord.ButtonStyle.red,
                row=0
            )
            remove_button.callback = self.create_remove_product_callback(product)
            self.add_item(remove_button)

    def create_remove_product_callback(self, product):
        async def callback(interaction: discord.Interaction):
            self.navigator.cart.remove_product(product)
            await self.navigator.open_cart(interaction)
        return callback

    @discord.ui.button(
        label="Clear cart",
        style=discord.ButtonStyle.red,
        row=1
    )
    async def clear_cart(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        self.navigator.cart.clear_cart()
        await self.navigator.open_cart(interaction)

    @discord.ui.button(
        label="Back to catalog",
        style=discord.ButtonStyle.blurple,
        row=1
    )
    async def back_to_catalog(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ):
        await self.navigator.open_catalog(interaction)