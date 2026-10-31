from dataclasses import dataclass

from domain.product import Product

@dataclass
class CartItem:
    product: Product
    quantity: int = 1

    def total_price(self):
        return self.quantity * self.product.price