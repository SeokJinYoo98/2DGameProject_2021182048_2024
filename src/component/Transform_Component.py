import Component
class TransformComponent(Component):
    def __init__(self, x=0, y=0, rotation=0, scaleX=0, scaleY=0):
        super().__init__()
        self.__position = [x, y]
        self.__rotation = rotation
        self.__scale = [scaleX, scaleY]
        
    def position(self):
        return self.__position
    def position(self, value):
        self.__position = value
    def rotation(self):
        return self.__rotation
    def rotation(self, value):
        self.__rotation = value
    def scale(self):
        return self.__scale
    def scale(self, value):
        self.__scale = value
    def add_translate(self, dx, dy):
        self.__position[0] += dx
        self.__position[1] += dy
    def add_rotate(self, delta):
        self.__rotation += delta
    def add_scale(self, sx, sy):
        self.__scale += sx
        self.__scale += sy