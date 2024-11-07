from gfw import *
from core import *

world = World(['bg', 'zombie', 'player', 'bullet', 'controller', 'UI'])

shows_bounding_box = True
shows_object_count = True

canvas_width = 1280
canvas_height = 1280

def enter():
    global playerController, collision, zombieZen, bg
    
    bg = RandomTileBackground('tile/Tiles.png', scale=6, margin=500)
    playerController = PlayerController_main(bg, False)
    zombieZen = ZombieZen(playerController.player) 
    collision = CollisionManager(playerController.player)
    
    world.append(bg, world.layer.bg)
    world.append(playerController, world.layer.controller)
    world.append(zombieZen, world.layer.controller)
    world.append(collision, world.layer.controller)
    
    world.bg = bg
    world.player = playerController.player
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
    if e.type == SDL_MOUSEBUTTONDOWN:
        if e.button == 3:
            zombieZen.zenZombies()
    playerController.handle_event(e)

if __name__ == '__main__':
    gfw.start_main_module()


        