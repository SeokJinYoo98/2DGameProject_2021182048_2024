import gfw
import random
from core import ItemManager
from zombies import *
class ZombieManager:
    DEAD_TIME = 0.5
    HIT_TIME = 0.05
    
    def __init__(self):
        self.world = gfw.top().world
        self.__zenTime = 0
    def draw(self):
        pass     
    def end(self):
        Zombie.BG = None
        Zombie.Target = None
        
    def update(self):
        self.__zenTime += gfw.frame_time
        if self.__zenTime >= 1:
            self.zenZombies()
            self.__zenTime = 0
        zombies = self.world.objects_at(self.world.layer.zombie)
        for z in zombies:
            self.__State_Check(z)
            
    def __State_Check(self, zombie):
        if zombie.state == "DEAD":
            self.__Death(zombie)
        elif zombie.state == "HIT":
            self.__Hit(zombie)
        elif zombie.state == 'WALK':
            self.__Walk(zombie)
        elif zombie.state == "ATTACK":
            self.__Attack(zombie)
            
    def __Death(self, zombie):
        if zombie.special_Range != None:
            zombie.spcial_Range = None
            
        zombie.animTime += gfw.frame_time
        if zombie.animTime >= ZombieManager.DEAD_TIME:
            ItemManager.CreateItem(zombie.x, zombie.y)
            zombie._erase()
                    
    def __Hit(self, zombie):
        zombie.animTime += gfw.frame_time
        if zombie.animTime >= ZombieManager.HIT_TIME:
            zombie.animTime = 0
            if zombie.hp <= 0:
                zombie._do_DEAD()
            else:
                zombie._do_WALK()
                
    def __Attack(self, zombie):
        zombie.special_Function()
        
    def __Walk(self, zombie):
        zombie.toTarget()     
   
                
    def zenZombies(self):
        x, y = 0, 0
        where = random.randint(0, 4)
        player = self.world.player
        if where <= 1:
            x = player.x - random.uniform(-player.x, player.x)
            if where == 1:
                y = player.y - 800
            else:
                y = player.y + 800
        else:
            y = player.y - random.uniform(-player.y, player.y)
            if where == 2:
                x = player.x - 800
            else:
                x = player.x + 800
    
        type = random.randint(0, 10)
        zombie = None

        if type == 0:
            zombie = ZombieT(x, y)
        elif type == 1:
            zombie = ZombieR(x, y)
        else:
            zombie = ZombieD(x, y)

        self.world.append(zombie, self.world.layer.zombie)
