from gfw import *
from pico2d import *
import scenes.menu_scene as menu_secne
import sys
self = sys.modules[__name__]

canvas_width = 1280
canvas_height = 1280

center_x = canvas_width // 2
center_y = canvas_height // 2

world = World(['bg', 'cards'])

class b(gfw.Sprite):
    def __init__(self, x, y, text):
        super().__init__('cards/SkillCardBase.png', x, y)
        self.is_mouse_on = False
        self.Frames = {
        "Non": (0, 0, 48, 62),
        "Click": (49, 0, 48, 62)
        }
        self.height *= 3
        self.width *= 6
        self.string = text
    def draw(self):
        frame = self.Frames["Click"]
        if not self.is_mouse_on: frame = self.Frames['Non']
        self.image.clip_draw(*frame, self.x, self.y, self.width, self.height)
        gfw.font.draw_centered_text(font, self.string, self.x + 10, self.y + 60)
        gfw.font.draw_centered_text(font, "[E N D I N G]", center_x, center_y + 400)
    def is_mouse_in_card(self, mx, my):
        l, b, r, t = self.get_bb()
        if l < mx and mx < r:
            if b <= my and my <= t:
                self.is_mouse_on = True
                return
        self.is_mouse_on = False    
def enter():
    global stB, exitB
    stB = b(center_x, center_y - 100, "Menu")
    exitB = b(center_x, center_y - 400, "Exit")
    world.append(HorzFillBackground('tile/Title.jpg'), world.layer.bg)
    world.append(stB, world.layer.cards)
    world.append(exitB, world.layer.cards)
    global font
    font = gfw.font.load('neodgm.TTF', 128)
    global mx, my
    mx, my = 0, 0
def exit():
    pass

def update():
    pass

def draw():
    pass
    
def handle_event(e):
    if e.type == SDL_MOUSEMOTION:
        mx,  my = e.x, get_canvas_height() - e.y
        stB.is_mouse_in_card(mx, my)
        exitB.is_mouse_in_card(mx, my)
    if e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                if stB.is_mouse_on:
                    gfw.change(menu_scene)
                elif exitB.is_mouse_on:
                    gfw.quit()   
        

def pause(): pass
def resume(): pass

if __name__ == '__main__':
    gfw.start_main_module()