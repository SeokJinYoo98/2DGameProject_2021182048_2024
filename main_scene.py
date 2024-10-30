from pico2d import * 
import gfw.gfw

from actor import Actor
from PlayerController import PlayerController

world = gfw.World(['player', 'bullet', 'controller'])

canvas_width = 800
canvas_height = 600

def enter():
    global player
    player = Actor()
    world.append(player, world.layer.player)
    global playerController
    playerController = PlayerController(player) 
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


        