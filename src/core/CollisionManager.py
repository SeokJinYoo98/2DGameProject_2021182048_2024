import gfw
class CollisionManager:
    def __init__(self):
        self.world = gfw.top().world
 
    def draw(self):
        pass
    
    def update(self):
        self.__collision_check()

    def __collision_check(self):
        player = self.world.player
        self.__check_Zombie(player)
        self.__check_Player(player)
        
    def __check_Zombie(self, player):
        zombies = self.world.objects_at(self.world.layer.zombie)
        for zombie in zombies:
            if not zombie.collType: continue
            self.__zombie_player(zombie, player)
            self.__zombie_bullet(zombie)
            
    def __zombie_player(self, zombie, player):
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
       
    def __player_item(self, player, item):
        if gfw.collides_circle(player, item):
            item.setTarget(player)
        else:
            item.deleteTarget()
        if gfw.collides_box(player, item):
            item.special_Function(player)            

    def __is_Hit_Bullet(self, target):
        bullets = self.world.objects_at(self.world.layer.bullet)
        for bullet in bullets:
            if gfw.collides_box(target, bullet):
                target.collide() 
                bullet.collide()
            
    def __is_Collide(self, source, target):
        if (gfw.collides_box(source, target)):
            source.collide()
            target.collide()
            
    