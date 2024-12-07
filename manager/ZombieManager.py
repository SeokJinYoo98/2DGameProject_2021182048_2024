import gfw
import random
from manager import ItemManager
from zombies import *

# Generator와 분리하고, 레벨당 스폰은 Genrator가 담당하게 변경하자.
class ZombieManager:
    DEAD_TIME = 0.2
    HIT_TIME = 0.07
    GENTIME = [
        1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1
    ]
    SPAWN_POINT = ('Up', 'Down', 'Left', 'Right')
    def __init__(self):
        self.world = gfw.top().world
        self.__zenTime = 0
        self.level = 0
        self.__time = 60
        self.end_ = False
        
    def draw(self):
        pass     
    def end(self):
        Zombie.BG = None
        Zombie.Target = None
        
    def update(self):
        if self.end_:
            Zombie.Target = None
            return
        self.__time -= gfw.frame_time
        if self.__time <= 0:
            self.level = (self.level + 1) % 10
            self.__time = 60
            print("LevelUp")
            
        self.__zenTime += gfw.frame_time
        if self.__zenTime >= ZombieManager.GENTIME[self.level]:
            self.zenZombies()
            self.__zenTime = 0
            
        zombies = self.world.objects_at(self.world.layer.zombie)
        for z in zombies:
            self.__State_Check(z)
  
    def __State_Check(self, zombie):
        if zombie.state is None: return
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
        if self.world.count_at(self.world.layer.zombie) >= 400: 
            return
        
        x, y = self.__getSpawnPoint()
        zombies = self.__addZombies(x, y)
        
        for zombie in zombies:
            self.world.append(zombie, self.world.layer.zombie)
        
    def __getSpawnPoint(self):
        player = self.world.player
        x, y = player.x, player.y
        
        where = random.choice(ZombieManager.SPAWN_POINT)
        
        if where == 'Up':
            x += random.randint(-612, 612)
            y += 800
        elif where == 'Down':
            x += random.randint(-612, 612)
            y -= 800
        elif where == 'Left':
            x -= 800
            y += random.randint(-612, 612)
        else:
            x += 800
            y += random.randint(-612, 612)
        
        return x, y
    
    def __addZombies(self, x, y):
        zombies = []
        if self.level == 0:
            zombies.append(ZombieD(x, y))
            
        elif self.level < 5:
            index = random.randint(0, 5)
            if index == 0:
                zombies.append(ZombieR(x, y))
            elif index == 1:
                zombies.append(ZombieT(x, y))
            else:
                zombies.append(ZombieD(x, y))
                
        elif self.level <= 7:
            index = random.randint(0, 1)
            if index == 0:
                zombies.append(ZombieR(x, y))
            else:
                zombies.append(ZombieT(x, y))
            zombies.append(ZombieD(x, y))
            
        elif self.level <= 8:
            index = random.randint(0, 1)
            if index == 0:
                zombies.append(ZombieR(x, y))
            else:
                zombies.append(ZombieT(x, y))
            zombies.append(ZombieD(x, y))
            zombies.append(ZombieD(x, y))
            
        else:
            zombies.append(ZombieD(x, y))
            zombies.append(ZombieD(x, y))
            zombies.append(ZombieT(x, y))
            zombies.append(ZombieR(x, y))

        return zombies
    
