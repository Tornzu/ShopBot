from datetime import datetime, timedelta

class AdminSessionService:
    def __init__(self):
        self.sessions = {}

    def create_session(self, discord_user_id: int):
        expires_at = datetime.now() + timedelta(minutes=30)
        self.sessions[discord_user_id] = expires_at

    def is_authenticated(self, discord_user_id: int) -> bool:
        expires_at = self.sessions.get(discord_user_id)
        if expires_at is None:
            return False
        if datetime.now() > expires_at:
            self.logout(discord_user_id)
            return False
        return True

    def logout(self, discord_user_id: int):
        self.sessions.pop(discord_user_id)