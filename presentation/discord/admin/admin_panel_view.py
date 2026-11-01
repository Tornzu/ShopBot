import discord


class AdminPanelView(discord.ui.View):
    def __init__(self, session_service):
        super().__init__(timeout=1800)
        self.session_service = session_service

    @discord.ui.button(
        label="Manage",
        style=discord.ButtonStyle.primary,
        emoji="📦"
    )
    async def manage_products(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.session_service.is_authenticated(interaction.user.id):
            await interaction.response.send_message("Session expired, please login again.", ephemeral=True)
            return
        await

    @discord.ui.button(
        label="Logout",
        style=discord.ButtonStyle.danger,
        emoji="🚪",
    )
    async def logout(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.session_service.is_authenticated(interaction.user.id):
            await interaction.response.send_message("Not logged in", ephemeral=True)
            return
        await interaction.response.send_message("Logged out", ephemeral=True)

