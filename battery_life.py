class Battery:
    def __init__(self, model, rate):
        self.model = model
        self.rate = rate
        self.power = 100

    def use_battery(self, seconds):
        used_power = self.rate * seconds
        self.power -= used_power
        return f'{used_power} power used;\n{self.power} remaining'


my_battery = Battery('Duracell', 0.009)
print(my_battery.use_battery(300))
