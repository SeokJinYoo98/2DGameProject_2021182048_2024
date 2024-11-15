from zombies import Zombie
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
            (0, 19, 19, 19)
        ]
    }
    FRAME_INFO = {
        # Frame Index Count, fps
        'IDLE': (1, 1 / 2),
        'WALK': (2, 1 / 4),
        'HIT': (1, 1 / 2),
        'DEAD': (1, 1 / 2),
        'ATTACK': (1, 1 / 2)
    }
    
    def __init__(self, x, y):
        fileName = 'zombie/zombieR.png'
        super().__init__(fileName, x, y, ZombieR)
        self.special_Range = 400
        
    def special_Function(self):
        if Zombie.Target is None: return
        
        # 거리 유지
        
        # 공격
        pass
