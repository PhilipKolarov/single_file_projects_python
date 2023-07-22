from abc import ABC, abstractmethod


class Juice(ABC):
    def __init__(self, quantity, pulp):
        self.quantity = quantity
        self.pulp = pulp

    @property
    def has_pulp(self):
        return self.pulp

    def drink(self, drink_quantity):
        self.quantity -= drink_quantity
        return self.quantity

    def add(self, added_quantity):
        self.quantity += added_quantity
        return self.quantity

    @abstractmethod
    def __str__(self):
        pass
