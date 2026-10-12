import discord

from domain.cart import Cart


class CartView(discord.ui.View):
    def __init__(self, navigator, cart: Cart):
        super().__init__()
        self.navigator = navigator

        if not cart.items:
            self.remove_item(self.clear_cart)

        for index, item in enumerate(cart.items):
            decrease_button = discord.ui.Button(
                label=f"- {item.product.name}",
                style=discord.ButtonStyle.red,
                row=index
            )
            increase_button = discord.ui.Button(
                label=f"+ {item.product.name}",
                style=discord.ButtonStyle.green,
                row=index
            )

            decrease_button.callback = self.create_decrease_product_callback(item.product.id)
            self.add_item(decrease_button)

            increase_button.callback = self.create_increase_product_callback(item.product.id)
            self.add_item(increase_button)

    def create_decrease_product_callback(self, product_id: int):
        async def callback(interaction: discord.Interaction):
            self.navigator.cart_service.decrease_quantity(
                user_id=interaction.user.id,
                product_id=product_id
            )
            await self.navigator.open_cart(interaction)
        return callback

    def create_increase_product_callback(self, product_id: int):
        async def callback(interaction: discord.Interaction):
            self.navigator.cart_service.add_product(
                user_id=interaction.user.id,
                product_id=product_id
            )
            await self.navigator.open_cart(interaction)
        return callback

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
        self.navigator.cart_service.clear_cart()
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