from abc import ABC, abstractmethod
from domain.cart import Cart

class CartRepository(ABC):
    @abstractmethod
    async def get_by_user_id(self, user_id: int) -> Cart | None:
        pass

    @abstractmethod
    async def create(self, cart: Cart) -> None:
        pass

    @abstractmethod
    async def update(self, cart: Cart) -> None:
        pass