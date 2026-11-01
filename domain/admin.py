import datetime
from dataclasses import dataclass


@dataclass
class Admin:
    id: int
    discord_user_id: int
    password_hash: str
    is_active: bool
    created_at: datetime
