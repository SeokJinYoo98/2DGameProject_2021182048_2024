import Component
import gfw
import weakref
import math

class Transform(Component):
    def __init__(self, x=0, y=0, rotation=0, scale_x=0, scale_y=0, velocity=100):
        self.position = [0, 0]
        self.rotation = rotation
        self.scale = [scale_x, scale_y]
        self.mag = [1, 1]
        self.direction = [0, 0]
        self.velocity = velocity
    def move(self):
        self.position[0] += self.direction[0] * self.velcity * gfw.frame_time
        self.position[1] += self.direction[1] * self.velcity * gfw.frame_time
    def add_rotate(self, angle):
        self.rotation += angle    
    def set_position(self, x, y):
        self.position = [x, y]
    def set_direction(self, dx, dy):
        self.direction = [dx, dy]
    def update(self):
        self.move()  
                   
class Transform_Target(Component):
    def __init__(self, x=0, y=0, rotation=0, scale_x=0, scale_y=0, target=None):
        super().__init__(x, y, rotation, scale_x, scale_y)
        self.target = weakref.ref(target)
        self.flip = ' '
    def set_target(self, target):
        self.target = weakref(target)
    def rotate_to_target(self):
        if self.target is None: return
        dx, dy = self.__get_dir()
        self.__set_flip(dx)
        self.rotation = math.atan2(dy, dx)
    def move_to_target(self):
        if self.__get_target() is None: return
        

        
    def __set_flip(self, dx):
        if dx < 0: self.flip = 'h'
        else: self.flip = ' '
    def __get_dir(self):
        target_ref = self.target()
        tx, ty = target_ref.position
        return tx - self.position[0], ty - self.position[1]
    def __get_target(self):
        return self.target()       