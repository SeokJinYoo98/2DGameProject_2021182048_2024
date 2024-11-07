from zombies import Zombie
class ZombieT(Zombie):
    Target = None
    BG = None
    Hp = 3
    Speed = 110
    ATTACK_RANGE = 200
    DASH_Speed = 2
    FRAMES = {
        'IDLE': [ 
            (19, 0, 19, 19)
        ],
        'WALK': [ 
            (0, 38, 19, 19), (19, 38, 19, 19), (38, 38, 19, 19), 
            (0, 19, 19, 19), (19, 19, 19, 19), (38, 19, 19, 19)  
        ],
        'HIT': [
            (0, 0, 19, 19)
        ],
        'DEAD': [
            (19, 0, 19, 19)
        ]
    }
    FRAME_INFO = {
        # Frame Index Count, fps
        'IDLE': (1, 1 / 2),
        'WALK': (6, 1 / 12),
        'HIT': (1, 1 / 2),
        'DEAD': (1, 1 / 2)
    }
    
    def __init__(self, x, y):
        fileName = 'zombie/zombieT.png'
        super().__init__(fileName, x, y, ZombieT)
