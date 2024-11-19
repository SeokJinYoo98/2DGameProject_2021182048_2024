from gfw import *
from core import Player, RandomTileBackground, Player_Controller_main

world = World(['bg', 'player', 'ui'])

shows_bounding_box = True
shows_object_count = True

canvas_width = 1280
canvas_height = 1280

def enter():
    
    world.player = Player()
    world.bg = RandomTileBackground('tile/Tiles.png', scale=6, margin=500)
    world.append(world.player, world.layer.player)
    world.append(world.bg, world.layer.bg)
    global pc
    pc = Player_Controller_main()
def exit(): 
    world.clear()
    print('[main.exit()]')

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    pc.handle_event(e)
    pass

if __name__ == '__main__':
    gfw.start_main_module()