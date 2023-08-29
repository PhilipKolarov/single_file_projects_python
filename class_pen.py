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
