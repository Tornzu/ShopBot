import discord

from application.cart_service import CartService
from application.product_service import ProductService
from application.repositories.cart_repository import CartRepository
from domain.cart import Cart
from domain.product import Product
from presentation.discord.views.cart_view import CartView
from presentation.discord.views.catalog_view import CatalogView
from presentation.discord.views.product_details_view import ProductDetailsView


class ShopNavigator:
    def __init__(
        self,
        product_service: ProductService,
        cart_service: CartService
    ):
        self.product_service = product_service
        self.cart_service = cart_service

    async def open_catalog(self, interaction: discord.Interaction):
        products = self.product_service.get_all_products()

        await interaction.response.edit_message(
            content="Choose a product: ",
            view=CatalogView(navigator=self, products=products)
        )

    async def open_product_details(
        self,
        interaction: discord.Interaction,
        product_id: int,
        message: str | None = None
    ):
        product = self.product_service.get_product(product_id)
        if product is None:
            await interaction.response.edit_message(
                content="Product not found",
                view=None
            )
            return

        content=(
            f"Product: {product.name}\n"
            f"Price: ${product.price}\n"
            f"Description: {product.description}"
        )
        if message:
            content += f"\n\n{message}"

        await interaction.response.edit_message(
            content=content,
            view=ProductDetailsView(navigator=self, product=product)
        )

    async def open_cart(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        cart = self.cart_service.get_cart(user_id)

        if not cart.items:
            content = "Your cart is empty"
        else:
            item_text = "\n".join(
                f"{item.product.name} - "
                f"${item.product.price} x {item.quantity}"
                f"= ${item.total_price()}"
                for item in cart.items
            )
            content = (
                f"Your cart: \n \n" 
                f"{item_text}\n \n"
                f"Total price: ${cart.total_price()}"
            )

        await interaction.response.edit_message(
            content=content,
            view=CartView(navigator=self, cart=cart)
        )