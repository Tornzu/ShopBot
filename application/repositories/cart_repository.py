from abc import ABC, abstractmethod
from domain.cart import Cart

class CartRepository(ABC):
    @abstractmethod
    async def get_by_user_id(self, user_id: int) -> Cart:
        pass

    @abstractmethod
    async def save(self, cart: Cart) -> None:
        pass