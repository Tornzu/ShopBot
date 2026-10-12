from application.repositories.cart_repository import CartRepository
from domain.cart import Cart


class InMemoryCartRepository(CartRepository):
    def __init__(self):
        self.carts = {}

    def get_by_user_id(self, user_id: int) -> Cart:
        if user_id not in self.carts:
            self.carts[user_id] = Cart(user_id)

        return self.carts[user_id]

    def save(self, cart: Cart) -> None:
        self.carts[cart.user_id] = cart