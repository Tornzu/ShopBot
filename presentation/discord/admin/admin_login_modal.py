import discord
from discord import Interaction
from discord._types import ClientT
impot

from presentation.discord.admin.admin_panel_view import AdminPanelView


class AdminLoginModal(discord.ui.Modal, title='Admin Login'):
    password = discord.ui.TextInput(
        label='Password',
        placeholder='Enter your password',
        required=True,
        style=discord.TextStyle.short,
    )

    def __init__(self, admin_service, admin_session_service):
        super().__init__()
        self.admin_service = admin_service
        self.admin_session_service = admin_session_service

    async def on_submit(self, interaction: Interaction[ClientT], /) -> None:
        await interaction.response.defer(ephemeral=True)
        user_id = interaction.user.id
        authenticated = await self.admin_service.authenticate(user_id, str(self.password.value))
        if not authenticated:
            await interaction.response.send_message("Invalid Credentials", ephemeral=True)
            return
        self.admin_session_service.create_session(user_id)
        await interaction.followup.send(
            "Welcome to admin panel",
            view=AdminPanelView(self.admin_session_servic),
            ephemeral=True,
        )
