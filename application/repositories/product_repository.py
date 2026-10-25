from abc import ABC, abstractmethod
from typing import List, Optional

from domain.product import Product


class ProductRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    async def get_by_id(self, product_id: int) -> Product | None:
        pass