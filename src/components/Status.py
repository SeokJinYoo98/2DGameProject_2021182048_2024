from component import Component
import weakref

    
class AIComponent(Component):
    def __init__(self, target):
        self.__target = weakref(target)
        pass


class AnimInfo_Component(Component):
    def __init__(self):
        pass
class Special_Status:
    def __init__(self, special_range=100, special_colltime=1):
        self.special_range = special_range
        self.special_colltime = special_colltime
    def get_special_info(self):
        return self.special_range, self.special_colltime
           
class LevelComponent(Component):
    def __init__(self, level=1, xp=0):
        self.__total_level = level
        self.__xp = xp
    def gain_xp(self, xp=1):
        self.xp += xp
                

    
class Player_Status(Special_Status):
    def __init__(self, hp=3, velocity=100):
        super().__init__(hp)
        self.Xp = 0
        self.speed = 150
        self.maxHp = 3
        self.hp = 3
        self.bullet_Scale = 2
        self.bullet_Range = 200
        self.bullet_Speed = 500
        self.bullet_ColCnt = 1
        self.bullet_RowCnt = 1
class Bullet_Status:
    def __init__(self):
        pass