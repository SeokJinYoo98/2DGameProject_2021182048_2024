from zombies import Zombie
import gfw
import random
class ZombieD(Zombie):
    Hp = 1
    Speed = 150
    ATTACK_RANGE = None
    FRAMES = {
        'IDLE': [ 
            (0, 0, 19, 19) 
        ],
        'WALK': [ 
            (0, 19, 19, 19), (19, 19, 19, 19), (38, 19, 19, 19) 
        ],
        'HIT': [
            (0, 0, 19, 19)
        ],
        'DEAD': [
            (38, 0, 19, 19)
        ]
    }
    FRAME_INFO = {
        # Frame Index Count, fps
        'IDLE': (1, 1 / 12),
        'WALK': (3, 1 / 6),
        'HIT': (1, 1/ 2),
        'DEAD': (1, 1 / 2)
    }
    ZOMBIE_TYPE = [
        1, 2, 3, 4
    ]
    def __init__(self, x, y):
        zomT = random.choice(ZombieD.ZOMBIE_TYPE)
        fileName = (f'zombie/zombie{zomT}.png')
        super().__init__(fileName, x, y, ZombieD)
        self.hit_Sound = gfw.sound.sfx('Hit1.wav')
        self.hit_Sound.set_volume(80)
        