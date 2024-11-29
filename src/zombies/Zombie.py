import gfw
from pico2d import *

class Zombie(gfw.Sprite):
    Target = None
    BG = None
    def __init__(self, fileName, x, y, TYPE):
        if Zombie.Target is None:
            Zombie.Target = gfw.top().world.player
        if Zombie.BG is None:
            Zombie.BG = gfw.top().world.bg
        super().__init__(fileName, x, y)

        self.special_Range = None
        self.hit_Sound = None
        # 애니메이션 관련
        self.state = None
        self.frame_index = 0
        self.frame_time = 0
        self.elapsed_time = 0

        self.flip = ' '
        self.TYPE = TYPE
        
        self.hp = self.TYPE.Hp
        
        self.animTime = 0
        
        self.mag = 1
        
        self._do_WALK()
          
    def update(self):
        pass

    def draw(self):
        self.anim()
        self.frame_index %= self.frame_count
        self.current_frame = self.TYPE.FRAMES[self.state][self.frame_index]
        x1, y1, x2, y2 = self.current_frame
        screen_pos = Zombie.BG.to_screen(self.x, self.y)
        self.image.clip_composite_draw(*self.current_frame,  0, self.flip, *screen_pos, w=50, h=50)
        if self.special_Range is not None:
            gfw.draw_circle(*screen_pos, self.special_Range, 0, 255, 0) 
               
    def anim(self):
        self.elapsed_time += gfw.frame_time
        if self.elapsed_time >= self.frame_time:
            self.elapsed_time = 0 
            self.frame_index += 1
                    
    def toTarget(self):
        if Zombie.Target is None: return
        tx, ty = int(Zombie.Target.x), int(Zombie.Target.y)
        zx, zy = int(self.x), int(self.y)
        
        dx = tx - zx
        dy = ty - zy
        
        if dx < 0:
            self.flip = 'h'
        else:
            self.flip = ' '
            
        normal = (dx ** 2 + dy ** 2) ** 0.5
        if normal != 0:
            dx /= normal
            dy /= normal
             
        self.x += dx * gfw.frame_time * self.TYPE.Speed * self.mag
        self.y += dy * gfw.frame_time * self.TYPE.Speed * self.mag
        
    def _change_Anim_Info(self, state):
        self.state = state
        self.frame_count = self.TYPE.FRAME_INFO[self.state][0]
        self.frame_time = self.TYPE.FRAME_INFO[self.state][1]
        self.animTime = 0   
        
    def _do_IDLE(self):
        if self.state != 'IDLE' and self.state != 'DEAD':
            self.collType = True
            self._change_Anim_Info("IDLE")
    def _do_WALK(self):
        if self.state != 'WALK' and self.state != 'DEAD':
            self.collType = True
            self._change_Anim_Info('WALK')
    def _do_HIT(self):
        if self.state != 'HIT' and self.state != 'DEAD':
            self.collType = False
            self._change_Anim_Info('HIT')
    def _do_DEAD(self):
        if self.state != 'DEAD':
            self.collType = False
            self._change_Anim_Info('DEAD')
    def _do_ATTACK(self):
           if self.state != 'ATTACK' and self.state != 'DEAD':
            self.collType = True
            self._change_Anim_Info('ATTACK') 
            
    def collide(self):
        self.hit_Sound.play()
        self._do_HIT()
        self.hp -= 1
    
    def get_bb(self):
        l = self.x - self.width // 3
        b = self.y - self.height // 2
        r = self.x + self.width // 3
        t = self.y + self.height // 2
        return l, b, r, t

    def _erase(self):
        world = gfw.top().world
        world.remove(self, world.layer.zombie)
        
    def special_Function(self):
        pass