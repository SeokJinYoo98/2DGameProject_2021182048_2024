import gfw
import random
from pico2d import *
class Zombie(gfw.Sprite):
    Target = None
    BG = None
    Hp = 1
    Speed = 100
    FRAMES = {
        'IDLE': [ 
            (0, 0, 19, 19) 
        ],
        'WALK': [ 
            (0, 19, 19, 19), (19, 19, 19, 19), (38, 19, 19, 19) 
        ],
        'HIT': [
            (19, 0, 19, 19), (0, 0, 19, 19)
        ],
        'DEAD': [
            (19, 0, 19, 19), (0, 0, 19, 19), (38, 0, 19, 19)
        ]
    }
    FRAME_INFO = {
        # Frame Index Count, fps
        'IDLE': (1, 1 / 12),
        'WALK': (3, 1 / 5),
        'HIT': (2, 1/ 2),
        'DEAD': (3, 1/ 3)
    }
    ZOMBIE_TYPE = [
        1, 2, 3, 4
    ]
    def __init__(self, x, y):
        if Zombie.BG is None:
            Zombie.BG = gfw.top().bg
        zomT = random.choice(Zombie.ZOMBIE_TYPE)
        super().__init__(f'zombie/zombie{zomT}.png', x, y)

        # 애니메이션 관련
        self.state = None
        self.frame_index = 0
        self.frame_time = 0
        self.elapsed_time = 0

        self._do_DEAD()
    
    def update(self):
        self.anim()
            
    def draw(self):
        current_frame = Zombie.FRAMES[self.state][self.frame_index]
        x1, y1, x2, y2 = current_frame
        screen_pos = Zombie.BG.to_screen(self.x, self.y)
        self.image.clip_composite_draw(*current_frame,  0, ' ', *screen_pos, w=50, h=50)     
               
    def anim(self):
        # 애니메이션 전환
        self.elapsed_time += gfw.frame_time
        if self.elapsed_time >= self.frame_time:
            self.elapsed_time = 0 
            # 다음 프레임으로 전환
            self.frame_index = (self.frame_index + 1) % self.frame_count
            
    def _change_Anim_Info(self):
        self.frame_count = Zombie.FRAME_INFO[self.state][0]
        self.frame_time = Zombie.FRAME_INFO[self.state][1]
        
    def _do_IDLE(self):
        if self.state != 'IDLE':
            self.state = "IDLE"
            self._change_Anim_Info()
    def _do_WALK(self):
        if self.state != 'WALK':
            self.state = 'WALK'
            self._change_Anim_Info()
    def _do_HIT(self):
        if self.state != 'HIT':
            self.state = 'HIT'
            self._change_Anim_Info()
    def _do_DEAD(self):
        if self.state != 'DEAD':
            self.state = 'DEAD'
            self._change_Anim_Info()