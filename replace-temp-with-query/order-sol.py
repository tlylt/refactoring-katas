# Thoughts

# The basic idea is to extract the calculation into a separate function, which is 
# easy to do in a class. Note that ideally the temp variable should be a read-only
# variable that is not reassigned later. The query function should also be pure, returning the same value each time it is called.

class Order:
    def __init__(self, quantity, item):
        self._quantity = quantity
        self._item = item
    
    def base_price(self):
        return self._quantity * self._item.price

    def discount_factor(self):
        discount_factor = 0.98
        if self.base_price() > 1000:
            discount_factor -= 0.03
        return discount_factor

    def price(self):
        return self.base_price() * self.discount_factor()