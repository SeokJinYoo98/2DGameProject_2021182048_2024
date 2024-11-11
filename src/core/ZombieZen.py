import gfw
import random
from core import ItemZen
from zombies import *
class ZombieZen:
    LEVEL_INCREASE = 30
    ZOMBIE_TYPE = 'D', 'R', 'T'
    DEAD_TIME = 0.5
    HIT_TIME = 0.2
    
    def __init__(self, player):
        # self.gameTime = 0
        # self.level = 1
        # self.totalZombies = self.level * ZombieZen.LEVEL_INCREASE
        # self.defaultZombies = 0
        # self.rangeZombies = 0
        # self.tankZombies = 0
        # self.time += gfw.time()
        self.player = player
        self.world = gfw.top().world

    def setZombiesCount(self):
        total = self.totalZombies
        self.tankZombies = self.level * 2
        self.rangeZombies = self.level * 2
        self.defaultZombies = total - self.tankZombies - self.rangeZombies
    def update(self):
        zombies = self.world.objects_at(self.world.layer.zombie)
        for z in zombies:
            if z.state == "DEAD":
                z.animTime += gfw.frame_time
                if z.animTime >= ZombieZen.DEAD_TIME:
                    ItemZen.CreateItem(z.x, z.y)
                    z._erase()
                    
                    
            elif z.state == "HIT":
                z.animTime += gfw.frame_time
                if z.animTime >= ZombieZen.HIT_TIME:
                    z.animTime = 0
                    if z.hp <= 0:
                        z._do_DEAD()
                    else:
                        z._do_WALK()
                           
            elif z.state == 'WALK':
                z.toTarget()
                
    def draw(self):
        pass
    
    def zenZombies(self):
        type = random.choice(ZombieZen.ZOMBIE_TYPE)
        
        x = self.player.x + random.choice([-500, 500])
        y = self.player.y + random.choice([-500, 500])

        zombie = None
        
        if type == 'D':
            zombie = ZombieD(x, y)
        elif type == 'R':
            zombie = ZombieR(x, y)
        elif type == 'T':
            zombie = ZombieT(x, y)
        
        self.world.append(zombie, self.world.layer.zombie)
    
    def LevelUp(self):
        self.level += 1
        self.setZombiesCount()
        