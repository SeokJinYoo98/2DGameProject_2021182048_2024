import Component

class MovementComponent(Component):
    def __init__(self, speed=100, mag=1):
        self.__speed = speed
        self.__mag = mag
        self.__direction = [0, 0]
        self.__flip = ' '
    def speed(self):
        return self.__speed
    def speed(self, value):
        self.__speed = value
    def mag(self):
        return self.__mag
    def mag(self, value):
        self.__mag = value
    def direction(self):
        return self.__direction
    def direction(self, value):
        self.__direction = value
    def move(self, frame_time):
        dx, dy = self.__direction
        m = self.__speed * self.__mag * frame_time
        move_x, move_y = dx * m, dy * m
        return move_x, move_y