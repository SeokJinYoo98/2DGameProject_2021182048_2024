from pico2d import * 
from gfw import *
from player import *
from utility import RandomTileBackground

world = World(['bg', 'player', 'bullet', 'controller', 'UI'])

shows_bounding_box = True
shows_object_count = True

canvas_width = 1280
canvas_height = 1280

def enter():
    global playerController, bg
    
    bg = RandomTileBackground('tile/Tiles.png', scale=6, margin=500)
    playerController = PlayerController_main(bg, False)
    
    world.append(bg, world.layer.bg)
    world.append(playerController, world.layer.controller)

    world.bg = bg
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


        