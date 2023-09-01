from abc import ABC, abstractmethod


class Guitar(ABC):

    def __init__(self, frets, battery, strings_qty):
        self.frets = frets
        self.battery = battery
        self.strings_qty = strings_qty
        self.tuning = self.determine_tuning()

    @abstractmethod
    def determine_tuning(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
