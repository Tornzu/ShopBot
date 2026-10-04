class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def clear_cart(self):
        self.products = []

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total