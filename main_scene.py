from pico2d import * 
import gfw.gfw

from actor import Actor

world = gfw.World(['player', 'bullet'])

canvas_width = 800
canvas_height = 600


def enter():
    global player
    player = Actor()
    world.append(player, world.layer.player)

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
        
    player.handle_event(e)

if __name__ == '__main__':
    gfw.start_main_module()

