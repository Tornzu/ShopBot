from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.orm import selectinload

from application.repositories.cart_repository import CartRepository
from domain.cart import Cart
from domain.cart_item import CartItem
from domain.product import Product
from infrastructure.database.models import UserModel, CartModel, CartItemModel


class SqlAlchemyCartRepository(CartRepository):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory

    async def get_by_user_id(self, user_id: int) -> Cart:
        async with self.session_factory() as session:
            result = await session.execute(
                select(CartModel)
                .join(CartModel.user)
                .where(UserModel.discord_user_id == user_id)
                .options(
                    selectinload(CartModel.items)
                    .selectinload(CartItemModel.product)
                )
            )

        model = result.scalars().one_or_none()
        if model is None:
            return None
        return self._to_domain(model, user_id)

    async def save(self, cart: Cart) -> None:
        pass

    @staticmethod
    def _to_domain(model: CartModel, user_id: int) -> Cart:
        cart = Cart(user_id=user_id)
        for item_model in model.items:
            product_model = item_model.product
            product = Product(
                id=product_model.id,
                name=product_model.name,
                price=product_model.price,
                description=product_model.description,
            )
            cart.items.append(
                CartItem(
                    product=product,
                    quantity=product_model.quantity,
                )
            )
        return cart