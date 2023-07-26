from abc import ABC, abstractmethod


class Juice(ABC):
    def __init__(self, quantity, pulp):
        self.quantity = quantity
        self.pulp = pulp
        if self.pulp:
            self.density = 1.25
        else:
            self.density = 1.04

    @property
    def has_pulp(self):
        return self.pulp

    @property
    def show_density(self):
        return self.density

    def drink(self, drink_quantity):
        self.quantity -= drink_quantity
        return self.quantity

    def add(self, added_quantity):
        self.quantity += added_quantity
        return self.quantity

    @abstractmethod
    def __str__(self):
        pass
