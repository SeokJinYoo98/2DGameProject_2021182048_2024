from zombies import Zombie
import gfw
class ZombieR(Zombie):
    Target = None
    BG = None
    Hp = 1
    Speed = 80
    ATTACK_COLLTIME = 1
    FRAMES = {
        'IDLE': [ 
            (0, 19, 19, 19)
        ],
        'WALK': [ 
            (0, 19, 19, 19), (19, 19, 19, 19)
        ],
        'HIT': [
            (38, 19, 19, 19)
        ],
        'DEAD': [
            (0, 0, 19, 19)
        ],
        'ATTACK': [
            (0, 19, 19, 19), (19, 19, 19, 19)
        ]
    }
    FRAME_INFO = {
        # Frame Index Count, fps
        'IDLE': (1, 1 / 2),
        'WALK': (2, 1 / 4),
        'HIT': (1, 1 / 2),
        'DEAD': (1, 1 / 2),
        'ATTACK': (2, 1 / 4)
    }
    
    def __init__(self, x, y):
        fileName = 'zombie/zombieR.png'
        super().__init__(fileName, x, y, ZombieR)
        self.special_Range = 400
        
    def special_Function(self):
        if Zombie.Target is None: return
        px, py = Zombie.Target.x, Zombie.Target.y
        
        dist = ((px - self.x) ** 2 + (py - self.y) ** 2) ** 0.5
        
        if dist <= self.special_Range - 50:
            # 거리 유지
            self.move_Back(px, py)
        else:
            # 공격
            pass   
    
    def move_Back(self, px, py):
        dx = self.x - px
        dy = self.y - py
        
        mag = (dx ** 2 + dy ** 2) ** 0.5
        if mag != 0:
            self.x += (dx / mag) * gfw.frame_time * ZombieR.Speed
            self.y += (dx / mag) * gfw.frame_time * ZombieR.Speed
        
