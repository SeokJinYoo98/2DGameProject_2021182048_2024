from component import Component
class Transform_Component(Component):
    def __init__(self, rotation=0, scaleX=1, scaleY=1):
        super().__init__()
        self.__rotation = rotation
        self.__scale = [scaleX, scaleY]
    @property
    def rotation(self):
        return self.__rotation
    @rotation.setter
    def rotation(self, delta):
        self.__rotation = delta
    @property
    def scale(self):
        return self.__scale
    @scale.setter
    def scale(self, x, y):
        self.__scale.x, self.__scale.y = x, y
    @property
    def position(self):
        return self.entity.x, self.entity.y
    @position.setter
    def position(self, x, y):
        self.entity.x, self.entity.y = x, y
        
    def add_translate(self, dx, dy):
        self.entity.x += dx
        self.entity.y += dy
    def add_rotate(self, delta):
        self.__rotation += delta
    def add_scale(self, sx, sy):
        self.__scale[0] += sx
        self.__scale[1] += sy
