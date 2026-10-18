import discord

from domain.product import Product


class ProductDetailsView(discord.ui.View):
    def __init__(self, navigator, product: Product):
        super().__init__()
        self.navigator = navigator
        self.product = product

    @discord.ui.button(
        label = "Add to cart",
        style = discord.ButtonStyle.green,
        row=0,
    )
    async def add_to_cart(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button,
    ):
        self.navigator.cart_service.add_product(
            user_id=interaction.user.id,
            product_id=self.product.id
        )

        await self.navigator.open_product_details(
            interaction,
            self.product.id,
            message="Successfully added to cart",
        )
    @discord.ui.button(
        label = "Back to catalog",
        style = discord.ButtonStyle.red,
        row=1,
    )
    async def back_to_catalog(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button,
    ):
        await self.navigator.open_catalog(interaction)

    @discord.ui.button(
        label = "View cart",
        style = discord.ButtonStyle.blurple,
        row=0,
    )
    async def cart(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button,
    ):
        await  self.navigator.open_cart(interaction)