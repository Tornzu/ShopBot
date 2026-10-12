from abc import ABC, abstractmethod
from domain.cart import Cart

class CartRepository(ABC):
    @abstractmethod
    def get_by_user_id(self, user_id: int) -> Cart:
        pass

    @abstractmethod
    def save(self, cart: Cart) -> None:
        pass