from abc import ABC, abstractmethod


class Guitar(ABC):
    STRING_BORDERS = [4, 9]
    STANDARD_NOTE_ORDER = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def __init__(self, model, frets, battery, strings_qty):
        self.model = model
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
            note_order = self.STANDARD_NOTE_ORDER
            beginning_index = note_order.index(string)
            for index, item in list(enumerate(note_order)):
                while index < beginning_index:
                    note_order.remove(item)
                    note_order.append(item)

            repetitions = self.frets // len(note_order) - 1
            additional_notes = self.frets % len(note_order)
            note_order_copy = note_order

            if repetitions == 1:
                for note in note_order_copy:
                    note_order.append(note)
            if additional_notes:
                for index in range(0, additional_notes):
                    note_order.append(note_order_copy[index])

            strings_notes_dict[string] = note_order

        return strings_notes_dict

    @abstractmethod
    def __repr__(self):
        pass
