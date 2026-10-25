from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.database.base import Base


class CartModel(Base):
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    user: Mapped["UserModel"] = relationship(back_populates="cart")

    items: Mapped[list["CartItemModel"]] = relationship(
        back_populates="cart",
        cascade="all, delete-orphan",
    )