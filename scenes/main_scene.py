from gfw import *
from core import *
from uis import *
import scenes.ending_scene as ending_scene

self = sys.modules[__name__]

world = World(['bg', 'zombie', 'zbullet', 'player', 'bullet', 'item',  'UI', 'cards', 'controller'])

# shows_bounding_box = True
# shows_object_count = True
canvas_width = 1024
canvas_height = 1024

def enter():
    SDL_ShowCursor(SDL_DISABLE)
    global playerController, zombieManager, LevelManager, collision
    bg = RandomTileBackground('tile/Tiles.png', scale=6, margin=300)
    playerController = PlayerController_main(bg)
    world.bg = bg
    world.player = playerController.player
    
  
    collision = CollisionManager()
    LevelManager = LevelUpManager()
    zombieManager = ZombieManager() 
    world.append(bg, world.layer.bg)
    world.append(playerController, world.layer.controller)
    world.append(zombieManager, world.layer.controller)
    world.append(collision, world.layer.controller)
    world.append(LevelManager, world.layer.controller)
    
    global Time
    Time = TimeUI()
    world.append(Time, world.layer.UI)
    world.append(HpUI(), world.layer.UI)
    world.append(XpUI(), world.layer.UI)
    world.append(InfoUI(zombieManager), world.layer.UI)
    key_states = SDL_GetKeyboardState(None)
    playerController.Init(key_states)   
    
    global bgm
    bgm = gfw.sound.music('BGM.wav')
    bgm.repeat_play()
    bgm.set_volume(30)

def update():
    print(f"{self.endTime=}")
    
def exit(): 
    SDL_ShowCursor(SDL_ENABLE)
    zombieManager.end()
    world.clear()
    bgm.stop()
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
        
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_t:
            Time.reduceTime()
            if zombieManager.level < 9:
                zombieManager.level += 1
def ending():
    gfw.change(ending_scene)

def Winner():
    zombieManager.end_ = True
    collision.end = True
    LevelManager.end = True
    playerController.end = True
    key_states = SDL_GetKeyboardState(None)
    playerController.KeyCheck(key_states)  
    Time.end = True
if __name__ == '__main__':
    gfw.start_main_module()


        