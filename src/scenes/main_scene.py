from gfw import *
from core import *

world = World(['bg', 'zombie', 'zbullet', 'player', 'bullet', 'item', 'controller', 'UI'])

shows_bounding_box = True
shows_object_count = True

canvas_width = 1280
canvas_height = 1280

def enter():
     
    SDL_ShowCursor(SDL_DISABLE)
    global playerController, zombieManager
    bg = RandomTileBackground('tile/Tiles.png', scale=6, margin=500)
    playerController = PlayerController_main(bg)
    zombieManager = ZombieManager() 
    collision = CollisionManager()

    world.append(bg, world.layer.bg)
    world.append(playerController, world.layer.controller)
    world.append(zombieManager, world.layer.controller)
    world.append(collision, world.layer.controller)
    
    world.bg = bg
    world.player = playerController.player
def exit(): 
    gfw.quit()
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
            zombieManager.zenZombies()
    playerController.handle_event(e)

if __name__ == '__main__':
    gfw.start_main_module()


        