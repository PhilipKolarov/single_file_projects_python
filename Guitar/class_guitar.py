from abc import ABC, abstractmethod


class Guitar(ABC):

    def __init__(self, frets, battery, strings_qty):
        self.frets = frets
        self.battery = battery
        self.strings_qty = strings_qty
        self.tuning = self.determine_standard_tuning()
        self.strings = self.determine_strings_notes()

    @abstractmethod
    def determine_standard_tuning(self):
        pass

    def determine_strings_notes(self):
        strings_notes_dict = {}

        for string in self.tuning:
            strings_notes_dict[string] = []

    def play_frets(self, **kwargs):
        for string, fret in kwargs.items():
            pass

    @abstractmethod
    def __repr__(self):
        pass
