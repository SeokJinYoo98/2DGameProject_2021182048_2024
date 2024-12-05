import gfw
from zombies import ZombieR
class CollisionManager:
    def __init__(self):
        self.world = gfw.top().world
        self.player = self.world.player
        self.end = False
    def draw(self):
        pass
    
    def update(self):
        if self.end:
            return
        
        self.__collision_check()

    def __collision_check(self):
        self.__check_Zombie(self.player)
        self.__check_Player(self.player)
        
    def __check_Zombie(self, player):
        zombies = self.world.objects_at(self.world.layer.zombie)
        for zombie in zombies:
            if zombie.state == 'DEAD' or zombie.state == 'HIT': continue
            if not zombie.collType: continue
            self.__zombie_player(zombie, player)
            self.__zombie_bullet(zombie)
            
    def __zombie_player(self, zombie, player):
        if not player.collType:
            zombie._do_WALK()
            return
        self.__is_Collide(zombie, player)
        if gfw.collides_circle(zombie, player):
            zombie._do_ATTACK()
        else:
            zombie._do_WALK()
        
    def __zombie_bullet(self, zombie):
        self.__is_Hit_Bullet(zombie)  
                
    def __check_Player(self, player):
        items = self.world.objects_at(self.world.layer.item)
        for item in items:
            self.__player_item(player, item)
        if not player.collType: return
        self.__player_bullet(player)
       
    def __player_item(self, player, item):
        if player.special_Range < 0:
            item.setTarget(player)
        elif gfw.collides_circle(player, item):
            item.setTarget(player)
        else:
            item.deleteTarget()
        if gfw.collides_box(player, item):
            item.special_Function(player)
                    
    def __player_bullet(self, player):
        self.__is_Hit_Bullet(player)
        
    def __is_Hit_Bullet(self, target):
        layer = self.world.layer.bullet
        if target == self.world.player:
            layer = self.world.layer.zbullet
            
        bullets = self.world.objects_at(layer)
        for bullet in bullets:
            if gfw.collides_box(target, bullet):
                target.collide() 
                bullet.collide()
            
    def __is_Collide(self, source, target):
        if (gfw.collides_box(source, target)):
            source.collide()
            target.collide()
            
    