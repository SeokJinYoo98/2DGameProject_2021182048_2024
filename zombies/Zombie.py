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
        self.state = 'IDLE'
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

    def end(self):
        Zombie.Target = None
        Zombie.BG = None
        
    def draw(self):
        self.anim()
        self.frame_index %= self.frame_count
        self.current_frame = self.TYPE.FRAMES[self.state][self.frame_index]
        screen_pos = Zombie.BG.to_screen(self.x, self.y)
        self.image.clip_composite_draw(*self.current_frame,  0, self.flip, *screen_pos, w=50, h=50)
               
    def anim(self):
        self.elapsed_time += gfw.frame_time
        if self.elapsed_time >= self.frame_time:  # 프레임 시간 초과 시에만 업데이트
            self.elapsed_time = 0 
            self.frame_index += 1
                    
    def toTarget(self):
        dx = Zombie.Target.x - self.x
        dy = Zombie.Target.y - self.y
        distance_squared = dx ** 2 + dy ** 2 

        if distance_squared == 0:
            return

        if (dx < 0 and self.flip == ' ') or (dx >= 0 and self.flip == 'h'):
            self.flip = 'h' if dx < 0 else ' '

        normal = distance_squared ** 0.5
        dx /= normal
        dy /= normal

        move_speed = gfw.frame_time * self.TYPE.Speed * self.mag
        self.x += dx * move_speed
        self.y += dy * move_speed
        
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