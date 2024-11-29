from gfw import *
from core import *
from uis import *
import scenes.ending_scene as ending_scene
world = World(['bg', 'zombie', 'zbullet', 'player', 'bullet', 'item',  'UI', 'cards', 'controller'])

shows_bounding_box = True
shows_object_count = True

canvas_width = 1024
canvas_height = 1024
def enter():
    SDL_ShowCursor(SDL_DISABLE)
    global playerController, zombieManager, LevelManager
    bg = RandomTileBackground('tile/Tiles.png', scale=6, margin=300)
    playerController = PlayerController_main(bg)
    world.bg = bg
    world.player = playerController.player
    
    zombieManager = ZombieManager() 
    collision = CollisionManager()
    LevelManager = LevelUpManager()
    
    world.append(bg, world.layer.bg)
    world.append(playerController, world.layer.controller)
    world.append(zombieManager, world.layer.controller)
    world.append(collision, world.layer.controller)
    world.append(LevelManager, world.layer.controller)
    
    world.append(TimeUI(), world.layer.UI)
    world.append(HpUI(), world.layer.UI)
    world.append(XpUI(), world.layer.UI)
    
    key_states = SDL_GetKeyboardState(None)
    if not key_states:
        pass
    else:
        playerController.Init(key_states)   
def exit(): 
    world.clear()
    print('[main.exit()]')

def pause():
    world.pause = True
    SDL_ShowCursor(SDL_ENABLE)
    print('[main.pause()]')

def resume():
    world.pause = False
    SDL_ShowCursor(SDL_DISABLE)
    print('[main.resume()]')

def handle_event(e):
    if world.pause:
        LevelManager.handle_event(e)
    else:
        playerController.handle_event(e)
def ending():
    SDL_ShowCursor(SDL_ENABLE)
    gfw.change(ending_scene)
    
if __name__ == '__main__':
    gfw.start_main_module()


        