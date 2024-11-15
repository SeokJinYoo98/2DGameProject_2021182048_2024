import gfw
import random
from src.core import ItemManager
from zombies import *
class ZombieManager:
    LEVEL_INCREASE = 30
    ZOMBIE_TYPE = 'D', 'R', 'T'
    DEAD_TIME = 0.5
    HIT_TIME = 0.2
    
    def __init__(self):
        self.world = gfw.top().world
        
    def draw(self):
        pass     
    
    def update(self):
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
        type = random.choice(ZombieManager.ZOMBIE_TYPE)
        
        x = self.world.player.x + random.choice([-500, 500])
        y = self.world.player.y + random.choice([-500, 500])

        zombie = None
        
        if type == 'D':
            zombie = ZombieR(x, y)
        elif type == 'R':
            zombie = ZombieR(x, y)
        elif type == 'T':
            zombie = ZombieR(x, y)
        
        self.world.append(zombie, self.world.layer.zombie)

        