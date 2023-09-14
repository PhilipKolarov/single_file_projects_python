class TrafficLights:
    def __init__(self, red_time, switch_time, green_time):
        self.red_time = red_time
        self.switch_time = switch_time
        self.green_time = green_time
        self.activated = False

    def activate(self):
        self.activated = True

    def deactivate(self):
        self.activated = False

