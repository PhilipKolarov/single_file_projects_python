class Speaker:
    def __init__(self, model, wattage, max_volume):
        self.model = model
        self.wattage = wattage
        self.max_volume = max_volume
        self.connected = False
        self.current_volume = 0

    def increase_volume(self, value):
        possible = self._volume_validator(value)
        if possible:
            return possible
        else:
            self.current_volume += value

    def decrease_volume(self, value):
        if self.current_volume - value < 0:
            self.current_volume = 0
        else:
            self.current_volume -= value

    def _volume_validator(self, change):
        if self.current_volume + change > self.max_volume:
            return f'The volume cannot cannot exceed {self.max_volume}!'
        return None

    def __repr__(self):
        return f'This {self.model} speaker is currently at {self.current_volume}db.'


my_speaker = Speaker('Mc Farlow', 30, 90)
my_speaker.increase_volume(50)
print(my_speaker.increase_volume(50))
my_speaker.decrease_volume(13)
print(my_speaker.__repr__())
