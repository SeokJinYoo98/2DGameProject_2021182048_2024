from pico2d import *
import gfw
import math
from player.Gun import Gun
from player.Bullet import Bullet
from uis import MagGauge

# 분리할 것 많음.
class Actor(gfw.Sprite):   
    PLAYER_FRAMES = {
        "IDLE": [
            (0, 0, 18, 20), (0, 0, 18, 20), (0, 0, 18, 20)
        ],
        "WALK": [
            (0, 42, 18, 20), (18, 42, 18, 20), (36, 42, 18, 20), 
            (0, 62, 18, 20), (18, 62, 18, 20), (36, 62, 18, 20),
        ],
        "BACK": [
            (36, 62, 18, 20), (18, 62, 18, 20), (0, 62, 18, 20), 
            (36, 42, 18, 20), (18, 42, 18, 20), (0, 42, 18, 20), 
        ],
        "DEAD": [
            (19, 0, 18, 20), (37, 0, 18, 20),
        ],
    }
    def __init__(self, path, bg):
        
        x = get_canvas_width() // 2
        y = get_canvas_height() // 2
        super().__init__(path, x, y)
        self.bg = bg
        # 애니메이션 관련
        self.state = None
        self.frame_index = 0
        self.frame_time = 0
        self.elapsed_time = 0
        # 아이템 획득
        self.special_Range = 100
        # 이동 관련
        self.dx, self.dy = 0, 0
        self.degree = 0
        self.flip = 'h'
        
        # 총 관련
        self.gun = Gun()
        # 총알 관련
        self.bullet_Time = 1
        # 레벨 관련
        self.maxXp = 5
        self.Xp = 0 # 레벨
        self.speed = 150 # 레벨업 요소
        self.maxHp = 3
        self.hp = 3 # 레벨업 요소
        self.bullet_Scale = 2 # 레벨업 요소  
        self.bullet_Cooltime = 1.056 # 레벨업 요소
        self.bullet_Range = 200 # 레벨업 요소
        self.bullet_Speed = 500 # 레벨업 요소
        self.bullet_ColCnt = 1 # 레벨업 요소
        self.bullet_RowCnt = 1 # 레벨업 요소
        self.bullet_Penetration = 1 # 관통
        self._do_IDLE()
        
        self.collidTime = 0
        
        self.hit_Sound = gfw.sound.sfx('Dead.wav')
        self.hit_Sound.set_volume(50)
        
        self.magTime = 3
        self.ismagTime = False
        self.magGauge = None
        
    def __del__(self):
        del self.gun
    def magneticTime(self):
        if self.magGauge is None:
            self.magGauge = MagGauge()
            world = gfw.top().world
            world.append(self.magGauge, world.layer.UI)
        self.ismagTime = True
        self.magTime = 3
        self.special_Range = -1
    # 업데이트            
    def update(self):
        if self.ismagTime:
            self.magTime -= gfw.frame_time
            if self.magTime <= 0:
                self.ismagTime = False
                self.special_Range = 100
        if self.state == "DEAD":
            self.dx, self.dy = 0, 0
            return
        if not self.collType:
            self.collidTime += gfw.frame_time
            if self.collidTime >= 1:
                self.collidTime = 0
                self.collType = True
        self.move()
        self.coolTime()
        self.anim()
    
    # 드로우        
    def draw(self):
        current_frame = Actor.PLAYER_FRAMES[self.state][self.frame_index]
        x1, y1, x2, y2 = current_frame
        screen_pos = self.bg.to_screen(self.x, self.y)
        self.image.clip_composite_draw(*current_frame,  0, self.flip, *screen_pos, w=50, h=50)
        if self.gun is not None:
            self.gun.draw_(self.flip, *screen_pos)
        #gfw.draw_circle(*screen_pos, self.special_Range, 0, 0, 255)
             
    ## ---------------------------------------------------------------------------
    def move(self):
        self.x += self.dx * self.speed * gfw.frame_time
        self.y += self.dy * self.speed * gfw.frame_time
        self.bg.show(self.x, self.y)
        
    def coolTime(self):
          # 사격 쿨타임 증가
        if self.bullet_Time <= self.bullet_Cooltime:
            self.bullet_Time += gfw.frame_time
            
    def anim(self):
         # 애니메이션 전환
        self.elapsed_time += gfw.frame_time
        if self.elapsed_time >= self.frame_time:
            self.elapsed_time = 0 
            # 다음 프레임으로 전환
            self.frame_index = (self.frame_index + 1) % self.frame_count
    def adjust_delta(self, x, y):
        self.dx += x
        self.dy += y
           
    def rotate(self, tx, ty):
        sX, sY = self.bg.from_screen(tx, ty)
        if sX - self.x > 0:
            self.flip = ' '
        else:
            self.flip = 'h'
        if self.gun is not None:
            self.gun.rotate(tx, ty, self.flip)
        
    # 총알 발사
    def fire(self):
        if self.state == "DEAD": return
        offsetX = 15
        offsetY = 15
        if self.bullet_Time < self.bullet_Cooltime: return
        self.gun.playSound()
        world = gfw.top().world
        bulletHalf = self.bullet_RowCnt // 2 
        bullets = [
            Bullet(
                self.x + offsetX * math.cos(self.gun.angle) * i,
                self.y + offsetY * math.sin(self.gun.angle) * i,
                self.gun.angle - 0.1 * (bulletHalf - j) if j < bulletHalf else self.gun.angle + 0.1 * (j - bulletHalf),
                self.bullet_Range,
                self.bullet_Speed,
                self.flip,
                self.bullet_Scale,
                self.bullet_Penetration
            )
            for i in range(self.bullet_ColCnt) 
            for j in range(self.bullet_RowCnt) 
        ]
        for bullet in bullets:
            world.append(bullet, world.layer.bullet)
        self.bullet_Time = 0
    def checkState(self):
        if self._isDead():
            self._do_DEAD()
        elif self._isMove():
            if self._isBack(): self._do_BackWALK()
            else: self._do_WALK()
        else:
            self._do_IDLE()
        
    def _isDead(self):
        if self.hp <= 0:
            return True
        return False
    
    def _isBack(self):
        if self.flip == ' ':
            if self.dx < 0:
                return True
        else:
            if self.dx > 0:
                return True
        return False
    
    def _isMove(self):
        if (abs(self.dx) + abs(self.dy)) > 0:
            return True
        return False
               
    def _update_frame_count(self):
        self.frame_count = len(Actor.PLAYER_FRAMES[self.state])
        
    def _change_state(self, name):
        if self.state != name or self.state == None:
            self.state = name
            self.frame_index = 0
            self.elapsed_time = 0
            self._update_frame_count()
    
    # 상태별 행동
    def _do_IDLE(self):
        if self.state == 'IDLE':
            return
        self._change_state('IDLE')
        self.frame_time = 1 / 5
            
    def _do_WALK(self):
        if self.state == 'WALK':
            return
        self._change_state("WALK")
        self.frame_time = 1 / 12
        
    def _do_BackWALK(self):
        if self.state == 'BACK':
            return
        self._change_state("BACK")
        self.frame_time = 1 / 12
        
    def _do_DEAD(self):
        if self.state == 'DEAD':
            return
        self._change_state("DEAD")
        self.frame_time = 1 / 3
        del self.gun
        self.gun = None
        self.dx, self.dy = 0, 0
    
    # 충돌
    def get_bb(self):
        l = self.x - self.width // 4
        b = self.y - self.height // 4
        r = self.x + self.width // 4
        t = self.y + self.height // 4
        return l, b, r, t
    
    def collide(self):
        self.hit_Sound.play()
        self.hp -= 1
        self.collType = False
    
