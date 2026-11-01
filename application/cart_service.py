from application.product_service import ProductService
from application.repositories.cart_repository import CartRepository
from application.repositories.product_repository import ProductRepository
from application.user_services import UserService
from domain.cart import Cart

class CartService:
    def __init__(
        self,
        cart_repository: CartRepository,
        product_service: ProductService,
        user_service: UserService
    ):
        self.cart_repository = cart_repository
        self.product_service = product_service
        self.user_service = user_service

    async def get_or_create_cart(self, user_id: int) -> Cart:
        await self.user_service.get_or_create(user_id)
        cart = await self.cart_repository.get_by_user_id(user_id)
        if cart is None:
            cart = Cart(user_id)
            await self.cart_repository.create(cart)
        return cart

    async def add_product(self, user_id: int, product_id: int) -> Cart:
        cart = await self.get_or_create_cart(user_id)
        product = await self.product_service.get_product(product_id)

        if product is None:
            raise ValueError("product not found")

        cart.add_product(product)
        await self.cart_repository.update(cart)
        return cart

    async def decrease_quantity(self, user_id: int, product_id: int) -> Cart:
        cart = await self.get_or_create_cart(user_id)
        cart.decrease_product(product_id)
        await self.cart_repository.update(cart)
        return cart

    async def clear_cart(self, user_id: int) -> Cart:
        cart = await self.get_or_create_cart(user_id)
        cart.clear_cart()
        await self.cart_repository.update(cart)
        return cart
