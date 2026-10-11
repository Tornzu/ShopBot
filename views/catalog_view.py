import discord


class CatalogView(discord.ui.View):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator

        for product in navigator.products:
            button = discord.ui.Button(
                label=product.name,
                style=discord.ButtonStyle.green
            )
            button.callback = self.create_product_callback(product)
            self.add_item(button)

    def create_product_callback(self, product):
        async def callback(interaction: discord.Interaction):
            await self.navigator.open_product_details(interaction, product)
        return callback

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
