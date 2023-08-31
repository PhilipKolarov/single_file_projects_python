class Pen:
    def __init__(self, color, lid, ink_capacity):
        self.color = color
        self.lid = lid
        self.lid_included = lid
        self.ink_capacity = ink_capacity

    def add_lid(self):
        if self.lid:
            return 'The lid is currently on.'
        elif not self.lid_included:
            return 'This pen does not have a lid.'
        else:
            self.lid = True
            return 'Lid added.'

    def take_off_lid(self):
        if not self.lid_included:
            return 'This pen does not have a lid.'
        elif not self.lid:
            return 'The lid is currently off.'
        else:
            self.lid = False
            return 'Lid taken off.'

    def write_word(self, word_count):
        if word_count * self.INK_PER_WORD <= self.ink_remaining:
            self.ink_remaining -= word_count * self.INK_PER_WORD

        else:
            print(f'Not enough ink for {word_count} words!')

    def __repr__(self):
        return f'Color - {self.color}; Ink remaining - {self.ink_remaining}'

pen = Pen('blue', True, 10000)
print(pen.__repr__())
print(pen.take_off_lid())
print(pen.write_word(145))
print(pen.add_lid())
print(pen.__repr__())
