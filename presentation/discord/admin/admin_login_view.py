import discord

from application.admin_services import AdminService
from application.admin_session_service import AdminSessionService
from presentation.discord.admin.admin_login_modal import AdminLoginModal


class AdminLoginView(discord.ui.View):
    def __init__(self, admin_service: AdminService, admin_session_service: AdminSessionService, user_id: int):
        super().__init__(timeout=300)
        self.admin_service = admin_service
        self.admin_session_service = admin_session_service
        self.user_id = user_id

    @discord.ui.button(
        label="login",
        style=discord.ButtonStyle.green,
    )

    async def login(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("access denied", ephemeral=True)
            return
        await interaction.response.send_modal(AdminLoginModal(self.admin_service, self.admin_session_service))

