from pico2d import *
import random
from gfw import *
import math

class Actor (Sprite):
    # x = 18, y = 20
    # maxX = 56, maxY = 83
    BULLET_INTERVAL = 0.25
    SPARK_INTERVAL = 0.05
    SPARK_OFFSET = 28
    
    PLAYER_FRAMES = {
        "IDLE": [
            (0, 20, 18, 20), (18, 21, 18, 20), (36, 21, 18, 20)
        ],
        "WALK": [
            (0, 42, 18, 20), (18, 42, 18, 20), (36, 42, 18, 20), 
            (0, 62, 18, 20), (18, 62, 18, 20), (36, 62, 18, 20),
        ],
        "DEAD": [
            (19, 0, 18, 20), (37, 0, 18, 20),
        ],
    }
   
    def __init__(self):
        x = get_canvas_width() // 2
        y = get_canvas_height() // 2
       
        super().__init__('assets/Sprites/Player/mainC.png', x, y)
       
        print(f"width={self.image.w}, height={self.image.h}")
        # 애니메이션 관련
        self.state = None
        self.frame_index = 0
        self.frame_time = 0
        self.elapsed_time = 0
        
        self._do_IDLE()
 
        # 이동 관련
        self.dx, self.dy = 0, 0
        self.speed = 100 # 100 pixels per second
        self.degree = 0
        self.flip = 'h'
        
        # 총알 관련
        self.bullet_time = 0
        self.spark_image = gfw.image.load('assets/Sprites/PropUI/Bullet1.png')
        self.bullet_range = 100 # range 10 pixel
    
    # 이벤트
    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            self._do_WALK()
            if e.key == SDLK_a:     self.dx = -1
            elif e.key == SDLK_d:   self.dx = 1
            elif e.key == SDLK_s:   self.dy = -1
            elif e.key == SDLK_w:   self.dy = 1
            
        elif e.type == SDL_KEYUP:
            self._do_IDLE()
            if e.key == SDLK_a:    self.dx = 0
            elif e.key == SDLK_d: self.dx = 0
            elif e.key == SDLK_s:  self.dy = 0
            elif e.key == SDLK_w:    self.dy = 0

        if e.type == SDL_MOUSEMOTION:
            if hasattr(self, 'degree'):
                self.rotate(e.x, get_canvas_height() - e.y - 1)
            
        self.bullet_time += gfw.frame_time
        if e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                if self.bullet_time >= Actor.BULLET_INTERVAL:
                    print('fire!')
                    self._fire()
        
    # 업데이트            
    def update(self):
   
        if self.dx < 0: self.flip = 'h'
        else: self.flip = ''
            
        self.x += self.dx * self.speed * gfw.frame_time
        self.y += self.dy * self.speed * gfw.frame_time
        
        # 애니메이션 전환
        self.elapsed_time += gfw.frame_time
        if self.elapsed_time >= self.frame_time:
            self.elapsed_time = 0 
            # 다음 프레임으로 전환
            self.frame_index = (self.frame_index + 1) % self.frame_count
        
    # 드로우        
    def draw(self):
        current_frame = Actor.PLAYER_FRAMES[self.state][self.frame_index]
        x1, y1, x2, y2 = current_frame

        self.image.clip_composite_draw(*current_frame,  0, self.flip, self.x, self.y,w=50, h=50)
        #self.image.clip_draw(0, 20, 18, 20, self.x, self.y)
                  
    ## ---------------------------------------------------------------------------        
    def rotate(self, tx, ty):
        self.degree = math.atan2(tx - self.x, ty - self.y)
        
    # 총알 발사
    def _fire(self):
        self.bullet_time = 0
        print('fire!')
        world = gfw.top().world
        world.append(Bullet(self.x, self.y, self.bullet_range), world.layer.bullet)
        
    # 상태 변경
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
        self._change_state('IDLE')
        self.frame_time = 1 / 5
            
    def _do_WALK(self):
        self._change_state("WALK")
        self.frame_time = 1 / 12
    
    def _do_DEAD(self):
        self._change_state("DEAD")
        self.frame_time = 1 / 3

class Bullet(Sprite):
    range = 10
    
    def __init__(self, x, y, bullet_range):
        super().__init__('assets/Sprites/PropUI/Bullet1.png', x, y)
        self.speed = 400 # pixels per second
        self.dist_travelled = 0
        self.layer_index = gfw.top().world.layer.bullet
        if bullet_range is not None:
            Bullet.range = bullet_range
        
    def update(self):
        move_dist = self.speed * gfw.frame_time
        self.y += move_dist
        
        self.dist_travelled += move_dist
        
        if self.dist_travelled >= self.range:
            gfw.top().world.remove(self)
        
    def draw(self):
        self.image.draw(self.x, self.y)

class Level():
    Range_Level = 0

class Gun():
    pass