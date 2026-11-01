from sqlalchemy import BigInteger, String, Boolean, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column
from datetime import datetime, timezone

from infrastructure.database.base import Base


class AdminModel(Base):
    __tablename__ = 'admin'

    id: Mapped[int] = mapped_column(primary_key=True)

    discord_user_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )