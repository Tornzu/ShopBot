from typing import List, Optional

from sqlalchemy.util import await_

from application.repositories.product_repository import ProductRepository
from domain.product import Product


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def get_all_products(self) -> List[Product]:
        return await self.product_repository.get_all()

    async def get_product(self, product_id: int) -> Product | None:
        return await self.product_repository.get_by_id(product_id)