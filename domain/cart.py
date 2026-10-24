from dataclasses import dataclass, field
from typing import List
from domain.cart_item import CartItem

@dataclass
class Cart:
    user_id: int
    items: List[CartItem] = field(default_factory=list)

    def find_item(self, product_id):
        for item in self.items:
            if item.product.id == product_id:
                return item
        return None

    def add_product(self, product):
        item = self.find_item(product.id)
        if not item:
            self.items.append(CartItem(product))
        else:
            item.quantity += 1

    def decrease_product(self, product_id):
        item = self.find_item(product_id)
        if not item:
            return
        if item.quantity > 1:
            item.quantity -= 1
        else:
            self.items.remove(item)

    def clear_cart(self):
        self.items.clear()

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.total_price()
        return total