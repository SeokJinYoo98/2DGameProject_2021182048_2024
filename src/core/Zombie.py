import gfw
from pico2d import *

class Zombie(gfw.Sprite):
    Target = None
    BG = None
    def __init__(self, fileName, x, y, TYPE):
        if Zombie.BG is None:
            Zombie.BG = gfw.top().bg
        # if Zombie.Target is None:
        #     Zombie.Target = gfw.top().layer.player
        super().__init__(fileName, x, y)

        # 애니메이션 관련
        self.state = None
        self.frame_index = 0
        self.frame_time = 0
        self.elapsed_time = 0

        self.TYPE = TYPE
        
        self._do_DEAD()
    
    def update(self):
        self.anim()
            
    def draw(self):
        self.current_frame = self.TYPE.FRAMES[self.state][self.frame_index]
        x1, y1, x2, y2 = self.current_frame
        self.screen_pos = Zombie.BG.to_screen(self.x, self.y)
        self.image.clip_composite_draw(*self.current_frame,  0, ' ', *self.screen_pos, w=50, h=50)     
               
    def anim(self):
        # 애니메이션 전환
        self.elapsed_time += gfw.frame_time
        if self.elapsed_time >= self.frame_time:
            self.elapsed_time = 0 
            # 다음 프레임으로 전환
            self.frame_index = (self.frame_index + 1) % self.frame_count
            
    def _change_Anim_Info(self):
        self.frame_count = self.TYPE.FRAME_INFO[self.state][0]
        self.frame_time = self.TYPE.FRAME_INFO[self.state][1]
        
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
            

    