from pico2d import * 
from gfw import *
from player import *


world = World(['bg', 'player', 'bullet', 'controller', 'UI'])

canvas_width = 1600
canvas_height = 800

def enter():
    global playerController, bg
    
    playerController = PlayerController_main(bg, False)
    
    world.append(playerController, world.layer.controller)
    

    
def exit(): 
    world.clear()
    print('[main.exit()]')

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    if e.type == SDL_KEYDOWN and e.key == SDLK_1:
        print(world.objects)
        
    playerController.handle_event(e)

if __name__ == '__main__':
    gfw.start_main_module()


        