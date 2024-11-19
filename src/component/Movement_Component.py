from component import Component, Transform_Component

class Movement_Component(Component):
    def __init__(self, speed=100, mag=1):
        super().__init__()
        self.__speed = speed
        self.__mag = mag
        self.__direction = [0, 0]
        self.__flip = ' '
        
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        self.__speed = value
    @property
    def mag(self):
        return self.__mag
    @mag.setter
    def mag(self, value):
        self.__mag = value
    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, value):
        self.__direction = value
    @property
    def flip(self):
        return self.__flip
    @flip.setter
    def flip(self, value):
        if self.__flip != value:
            self.__flip = value  
    def get_movement(self):
        return (self.__direction[0] * self.__speed * self.__mag,
                self.__direction[1] * self.__speed * self.__mag)              
    def get_movementX(self):
        return self.__direction[0] * self.__speed * self.__mag
    def get_movementY(self):
        return self.__direction[1] * self.__speed * self.__mag
    def add_dir(self, x, y):
        if self.__direction[0] != x:
            self.__direction[0] += x
        if self.__direction[1] != y:
            self.__direction[1] += y