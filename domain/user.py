from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    discord_user_id: int
    id : int | None = None