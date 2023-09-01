from abc import ABC, abstractmethod


class Guitar(ABC):
    STRING_BORDERS = [4, 9]

    def __init__(self, frets, battery, strings_qty):
        self.frets = frets
        self.battery = battery
        self.strings_qty = self._is_valid_strings_qty(strings_qty)
        self.tuning = self.determine_standard_tuning()
        self.strings = self.determine_strings_notes()

    def _is_valid_strings_qty(self, strings_qty):
        string_min = self.STRING_BORDERS[0]
        string_max = self.STRING_BORDERS[1]
        if strings_qty < string_min or strings_qty > string_max:
            raise AttributeError(f'Invalid number of strings! Please try again.')

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
