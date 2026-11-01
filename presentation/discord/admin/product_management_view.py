import discord


class ProductManagementView(discord.ui.View):
    def __init__(self, password: str):
        super().__init__()
        self.password = password

    @discord.ui.button(
        label="view products",
        style=discord.ButtonStyle.green,
        emoji="👁️"
    )

    async def view_products(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.navigator.open_catalog()
