class CartItem:
    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity
        
    def total_price(self):
        return self.quantity * self.product.price
