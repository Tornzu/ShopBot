#%%
from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import Base


class CartItemModel(Base):
    __tablename__ = "cart_item"

    id: Mapped[int] = mapped_column(primary_key=True,)

    product_id: Mapped[int] = mapped_column(
        ForeignKey("product.id"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    cart_id: Mapped[int] = mapped_column(
        ForeignKey("cart.id"),
        nullable=False,
    )

    cart: Mapped["CartModel"] = relationship(back_populates="items")

    product: Mapped["ProductModel"] = relationship()

    __table_args__ = (
        UniqueConstraint(
            "cart_id",
            "product_id",
        ),
    )