from pico2d import * 
from actor import Actor
from actor import Aim
import gfw.gfw
import gfw.world
class PlayerController:
    def __init__(self, player):
        self.player = player
        self.mouse_x = 0
        self.mouse_y = 0
        SDL_ShowCursor(SDL_DISABLE)
        self.aim = Aim()
        
    def update(self):
        self.player.rotate(self.mouse_x, self.mouse_y)
        
    def draw(self):
        self.aim.draw()
    
    def handle_event(self, e):
        if e.type == SDL_MOUSEMOTION:
            world = gfw.top()
            self.mouse_x,  self.mouse_y = e.x, world.canvas_height - e.y
            self.aim.setLoaction(self.mouse_x, self.mouse_y)
            
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_a:
                self.player.dx -= 1
            elif e.key == SDLK_d:
                self.player.dx += 1
            elif e.key == SDLK_w:
                self.player.dy += 1
            elif e.key == SDLK_s:
                self.player.dy -= 1
                
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_a:
                self.player.dx += 1
            elif e.key == SDLK_d:
                self.player.dx -= 1
            elif e.key == SDLK_w:
                self.player.dy -= 1
            elif e.key == SDLK_s:
                self.player.dy += 1
                