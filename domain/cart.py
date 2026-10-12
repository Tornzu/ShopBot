from domain.cart_item import CartItem


class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []

    def find_item(self, product_id):
        return (
            next(
                item
                for item in self.items
                if item.id == product_id
            ),
            None
        )

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