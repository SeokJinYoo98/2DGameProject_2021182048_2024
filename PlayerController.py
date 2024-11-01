from pico2d import * 
from actor import Actor
from actor import Aim
import gfw.gfw
import gfw.world
class PlayerController:
    def __init__(self): pass
    def update(self): pass
    def draw(self): pass
    def handle_event(self, e): pass
    
class PlayerController_main(PlayerController):
    def __init__(self, player):
        self.player = player
        SDL_ShowCursor(SDL_DISABLE)
        self.aim = Aim()
        
    def update(self):
        self.player.rotate(self.aim.x, self.aim.y)
        
    def draw(self):
        self.aim.draw()
    
    def handle_event(self, e):
        # 에임 설정
        if e.type == SDL_MOUSEMOTION:
            world = gfw.top()
            mouse_x,  mouse_y = e.x, world.canvas_height - e.y
            self.aim.setLoaction(mouse_x, mouse_y)
        
        # 사격 수행
        if e.type == SDL_MOUSEBUTTONDOWN:
            self.player.fire()
        
        
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_a:
                self.player.dx -= 1
            elif e.key == SDLK_d:
                self.player.dx += 1
            elif e.key == SDLK_w:
                self.player.dy += 1
            elif e.key == SDLK_s:
                self.player.dy -= 1
                
            self.player.checkState()
            
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_a:
                self.player.dx += 1
            elif e.key == SDLK_d:
                self.player.dx -= 1
            elif e.key == SDLK_w:
                self.player.dy -= 1
            elif e.key == SDLK_s:
                self.player.dy += 1
            self.player.checkState()
                
        
                