class Speaker:
    def __init__(self, model, wattage, max_volume):
        self.model = model
        self.wattage = wattage
        self.max_volume = max_volume
        self.connected = False
        self.current_volume = 0

    def increase_volume(self, value):
        self.current_volume += value

    def decrease_volume(self, value):
        self.current_volume -= value

    def __repr__(self):
        return f'This {self.model} speaker is currently at {self.current_volume}db.'


my_speaker = Speaker('Mc Farlow', 30, 90)
my_speaker.increase_volume(50)
print(my_speaker.__repr__())
