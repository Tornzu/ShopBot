from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from application.repositories.product_repository import ProductRepository
from domain.product import Product
from infrastructure.database.models import ProductModel


class SqlAlchemyProductRepository(ProductRepository):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory

    async def get_all(self) -> List[Product]:
        async with self.session_factory() as session:
            result = await session.execute(
                select(ProductModel)
            )
            models = result.scalars().all()
            return [
                self._to_domain(model)
                for model in models
            ]

    async def get_by_id(self, product_id: int) -> Product | None:
        async with self.session_factory() as session:
            model = await session.get(
                ProductModel,
                product_id
            )
            if model is None:
                return None
            return self._to_domain(model)


    @staticmethod
    def _to_domain(model: ProductModel) -> Product:
        return Product(
            id=model.id,
            name=model.name,
            price=model.price,
            description=model.description,
        )