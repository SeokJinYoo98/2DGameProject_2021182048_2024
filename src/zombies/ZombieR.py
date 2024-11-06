from zombies import Zombie
class ZombieR(Zombie):
    Target = None
    BG = None
    Hp = 1
    Speed = 90
    FRAMES = {
        'IDLE': [ 
            (0, 19, 19, 19) 
        ],
        'WALK': [ 
            (0, 19, 19, 19), (19, 19, 19, 19)
        ],
        'HIT': [
            (38, 19, 19, 19),
        ],
        'DEAD': [
            (0, 0, 19, 19)
        ]
    }
    FRAME_INFO = {
        # Frame Index Count, fps
        'IDLE': (1, 1 / 2),
        'WALK': (2, 1 / 4),
        'HIT': (1, 1 / 2),
        'DEAD': (1, 1 / 2)
    }

    def __init__(self, x, y):
        fileName = 'zombie/zombieR.png'
        super().__init__(fileName, x, y, ZombieR)
    
