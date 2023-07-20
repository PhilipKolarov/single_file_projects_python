class Juice:
    def __init__(self, quantity, pulp):
        self.quantity = quantity
        self.pulp = pulp

    def drink(self, drink_quantity):
        self.quantity -= drink_quantity
        return self.quantity

    def add(self, added_quantity):
        self.quantity += added_quantity
        return self.quantity

