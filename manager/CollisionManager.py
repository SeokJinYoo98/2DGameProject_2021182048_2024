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
        if self.end: return
        zombies = self.world.objects_at(self.world.layer.zombie)
        
        for zombie in zombies:
            if zombie.state == 'DEAD' or zombie.state == 'HIT': continue
            
            if self.player.collType:
                if gfw.collides_circle(zombie, self.player):
                    zombie._do_ATTACK()
                else:
                    zombie._do_WALK()
                    
                if gfw.collides_box(zombie, self.player):
                    zombie.collide()
                    self.player.collide()
                    continue
                
            if zombie.state == 'DEAD' or zombie.state == 'HIT': continue    
            bullets = self.world.objects_at(self.world.layer.bullet)
            for bullet in bullets:
                if gfw.collides_box(zombie, bullet):
                    zombie.collide()
                    bullet.collide()
                    break
                
        items = self.world.objects_at(self.world.layer.item)
        for item in items:
            if gfw.collides_box(self.player, item):
                item.special_Function(self.player)
            if self.player.special_Range < 0:
                if item.target is None:
                    item.target = self.player
            elif gfw.collides_circle(self.player, item):
                if item.target is None:
                    item.target = self.player
            else:
                if item.target is not None:
                    item.target = None
                
        if not self.player.collType: return
        bullets = self.world.objects_at(self.world.layer.bullet)
        for bullet in bullets:
            if gfw.collides_box(self.player, bullet):
                self.player.collide()
                bullet.collide()
                return

    # def __check_Zombie(self): pass


            
    # def __zombie_player(self, zombie):    
    #     if gfw.collides_circle(zombie, self.player):
    #         zombie._do_ATTACK()
    #     else:
    #         zombie._do_WALK()
            
    #     if gfw.collides_box(zombie, self.player):
    #         zombie.collide()
    #         self.player.collide()
    
    # def __check_Player(self):
    #     pass
       
    # def __player_item(self, item):
    #     if gfw.collides_box(self.player, item):
    #         item.special_Function(self.player)
    #         return
        
    #     if self.player.special_Range < 0:
    #         item.setTarget(self.player)
            
    #     elif gfw.collides_circle(self.player, item):
    #         item.setTarget(self.player)
    #     else:
    #         item.deleteTarget()
              
    # def __is_Hit_Bullet(self, target):
    #     layer = None
    #     if target == self.world.player:
    #         if not target.collType: return
    #         layer = self.world.layer.zbullet
    #     else:
    #         if target.state == 'DEAD' or target.state == 'HIT': return
    #         layer = self.world.layer.bullet
            
    #     bullets = self.world.objects_at(layer)
    #     for bullet in bullets:
    #         if gfw.collides_box(target, bullet):
    #             target.collide() 
    #             bullet.collide()
    #             return
            