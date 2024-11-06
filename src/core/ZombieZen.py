import gfw
import random as random
from zombies import ZombieD
from zombies import ZombieR
from zombies import ZombieT

class ZombieZen:
    LEVEL_INCREASE = 30
    ZOMBIE_TYPE = 'D', 'R', 'T'
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
        pass
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
        
        self.world.append(zombie, self.world.layer.zombies)
    
    def LevelUp(self):
        self.level += 1
        self.setZombiesCount()
        