class Torch:
    MAX_BATTERY = 100

    def __init__(self, color):
        self.color = color
        self.status = 'off'
        self.battery = self.MAX_BATTERY

    def switch(self):
        if self.status == 'on':
            self.status = 'off'
            self.battery -= 1
        else:
            self.status = 'on'
            self.battery -= 3

        return self.status

    def charge(self, qty):
        if qty > (self.MAX_BATTERY - self.battery):
            self.battery = 100
        else:
            self.battery += qty

        return f'Torch is now {self.battery}% charged.'

    def __repr__(self):
        return f'This {self.color} torch is now {self.status} and has {self.battery}% battery remaining.'


my_torch = Torch('red')
print(my_torch.switch())
print(my_torch.switch())
print(my_torch.switch())
print(my_torch.charge(5))
print(my_torch.switch())
print(my_torch.__repr__())
