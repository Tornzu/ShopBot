from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import Base


class UserModel(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)

    discord_user_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
    )

    cart: Mapped["CartModel"] = relationship(
        back_populates="user",
    )