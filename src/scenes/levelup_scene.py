from gfw import *
from core import Player, RandomTileBackground

world = World(['bg', 'player'])

shows_bounding_box = True
shows_object_count = True

canvas_width = 1280
canvas_height = 1280

def enter():
    world.palyer = Player()
    world.append(world.palyer, world.layer.player)

def exit(): 
    world.clear()
    print('[main.exit()]')

def pause():
    print('[main.pause()]')

def resume():
    print('[main.resume()]')

def handle_event(e):
    pass

if __name__ == '__main__':
    gfw.start_main_module()