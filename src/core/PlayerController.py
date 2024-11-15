from pico2d import * 
import gfw
from player import Actor
from player import Aim
 
class PlayerController:
    def __init__(self): pass
    def update(self): pass
    def draw(self): pass
    def handle_event(self, e): pass
    
class PlayerController_main(PlayerController):
    def __init__(self, bg):
        self.player = Actor('player/mainC.png', bg)
        self.aim = Aim()
        self.world = gfw.top().world
        world = gfw.top().world
        world.append(self.player, world.layer.player)
        world.append(self.aim, world.layer.UI)
        
    def update(self):
        self.player.rotate(self.aim.x, self.aim.y)
        self.player.checkState()
    
    def handle_event(self, e):
        # 에임 설정
        if e.type == SDL_MOUSEMOTION:
            mouse_x,  mouse_y = e.x, get_canvas_height() - e.y
            self.aim.setLoaction(mouse_x, mouse_y)
        
        # 사격 수행
        if e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                self.player.fire()
        
        # 이동 설정
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_a:
                self.player.adjust_delta(-1, 0)
            elif e.key == SDLK_d:
                self.player.adjust_delta(1, 0)
            elif e.key == SDLK_w:
                self.player.adjust_delta(0, 1)
            elif e.key == SDLK_s:
                self.player.adjust_delta(0, -1)
            
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_a:
                self.player.adjust_delta(1, 0)
            elif e.key == SDLK_d:
                self.player.adjust_delta(-1, 0)
            elif e.key == SDLK_w:
                self.player.adjust_delta(0, -1)
            elif e.key == SDLK_s:
                self.player.adjust_delta(0, 1)

    def Hit(self):
        self.player.collide()
