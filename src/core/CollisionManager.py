import gfw
class CollisionManager:
    def __init__(self, player):
        self.world = gfw.top().world
        self.player = player
    def draw(self):
        pass
    
    def update(self):
        zombies = self.world.objects_at(self.world.layer.zombie)

        if 0 < self.world.count_at(self.world.layer.zombie):
            self.check_Zombie(zombies)


    def check_Zombie(self, zombies):
        for z in zombies:
            if not z.collType: continue
            if gfw.collides_box(self.player, z):
                self.player.collide()
                z.collide()

            bullets = self.world.objects_at(self.world.layer.bullet)
            if self.world.count_at(self.world.layer.bullet) <= 0:
                continue
            for b in bullets:
                if gfw.collides_box(b, z):
                    b.collide()
                    z.collide()
                