from component import Component
class Transform_Component(Component):
    def __init__(self, rotation=0, scaleX=0, scaleY=0):
        super().__init__()
        self.__rotation = rotation
        self.__scale = [scaleX, scaleY]
        
    
    def set_position(self, x, y):
        if self.entity:
            self.entity.x = x
            self.entity.y = y
    def set_scale(self, value):
        self.__scale = value
    def set_rotation(self, value):
        self.__rotation = value
        
    def get_position(self):
        if self.entity: return [self.entity.x, self.entity.y]
        return [0, 0]    
    def get_scale(self):
        return self.__scale
    def get_rotation(self):
        return self.__rotation
    
    def add_translate(self, dx, dy):
        self.entity.x += dx
        self.entity.y += dy
    def add_rotate(self, delta):
        self.__rotation += delta
    def add_scale(self, sx, sy):
        self.__scale[0] += sx
        self.__scale[1] += sy