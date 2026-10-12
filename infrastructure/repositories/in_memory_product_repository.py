from typing import List, Optional

from application.repositories.product_repository import ProductRepository
from domain.product import Product

class InMemoryProductRepository(ProductRepository):
    def __init__(self, products: List[Product]) -> None:
        self.products = products

    def get_all(self) -> List[Product]:
        return self.products

    def get_by_id(self, product_id: int) -> Optional[Product]:
        for product in self.products:
            if product.id == product_id:
                return product
        return None