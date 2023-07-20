class Juice:
    def __init__(self, quantity, pulp):
        self.quantity = quantity
        self.pulp = pulp
        self.taste = ''

    def drink(self, drink_quantity):
        self.quantity -= drink_quantity
        return self.quantity

    def add(self, added_quantity):
        self.quantity += added_quantity
        return self.quantity

    def __str__(self):
        message = f'This {self.taste}" juice is {self.quantity}.'
