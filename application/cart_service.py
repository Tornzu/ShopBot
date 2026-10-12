from application.repositories.cart_repository import CartRepository
from application.repositories.product_repository import ProductRepository
from domain.cart import Cart

class CartService:
    def __init__(
        self,
        cart_repository: CartRepository,
        product_repository: ProductRepository
    ):
        self.cart_repository = cart_repository
        self.product_repository = product_repository

    def get_cart(self, user_id: int) -> Cart:
        return self.cart_repository.get_by_user_id(user_id)

    def add_product(self, user_id: int, product_id: int) -> Cart:
        cart = self.cart_repository.get_by_user_id(user_id)
        product = self.product_repository.get_by_id(product_id)

        if product is None:
            raise ValueError("product not found")

        cart.add_product(product)
        self.cart_repository.save(cart)
        return cart

    def decrease_quantity(self, user_id: int, product_id: int) -> Cart:
        cart = self.cart_repository.get_by_user_id(user_id)
        cart.decrease_product(product_id)
        self.cart_repository.save(cart)
        return cart

    def clear_cart(self, user_id: int) -> Cart:
        cart = self.cart_repository.get_by_user_id(user_id)
        cart.clear_cart()
        self.cart_repository.save(cart)
        return cart
