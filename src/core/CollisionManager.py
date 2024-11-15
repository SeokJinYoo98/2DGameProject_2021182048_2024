import gfw
class CollisionManager:
    def __init__(self):
        self.world = gfw.top().world
 
    def draw(self):
        pass
    
    def update(self):
        self.check_Zombie()


    def check_Zombie(self):
        zombies = self.world.objects_at(self.world.layer.zombie)
        if 0 < self.world.count_at(self.world.layer.zombie):
            for z in zombies:
                if not z.collType: continue
                if gfw.collides_box(self.world.player, z):
                    self.world.player.collide()
                    z.collide()

                bullets = self.world.objects_at(self.world.layer.bullet)
                if self.world.count_at(self.world.layer.bullet) <= 0:
                    continue
                for b in bullets:
                    if gfw.collides_box(b, z):
                        b.collide()
                        z.collide()
                        
    def check_Item(self):
        items = self.world.objects_at(self.world.layer.item)
        if (0 < self.world.count_at(self.world.layer.item)):
            for item in items:
                gfw.collides_circle(self.world.player, item)
                