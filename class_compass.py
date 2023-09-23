class Compass:
    MAX_DEGREES = 360

    def __init__(self, color):
        self.color = color
        self.current_degrees = 0

    def turn(self, degrees, direction):
        if direction == 'right' or direction == 'clockwise':
            self.current_degrees += degrees
        elif direction == 'left' or direction == 'anticlockwise':
            self.current_degrees = abs(self.current_degrees - degrees)
        else:
            return 'Direction not compatible! Must be one of the following: right, clockwise, left, anticlockwise.'

        self.current_degrees %= 360
