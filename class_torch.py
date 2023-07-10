class Torch:
    def __init__(self, color):
        self.color = color
        self.status = 'off'

    def switch(self):
        if self.status == 'on':
            self.status = 'off'
        else:
            self.status = 'on'
        return self.status

    def __repr__(self):
        return f'This {self.color} torch is now {self.status}.'


my_torch = Torch('red')
print(my_torch.switch())
print(my_torch.__repr__())
