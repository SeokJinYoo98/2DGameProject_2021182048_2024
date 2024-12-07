import gfw
from pico2d import *
import scenes.menu_scene as menu_scene

import sys
self = sys.modules[__name__]

#shows_bounding_box = True
#shows_object_count = True

canvas_width = 1024
canvas_height = 1024

center_x = canvas_width / 2
center_y = canvas_height / 2

world = gfw.World(2)



def enter():
    self.gauge = gfw.Gauge('progress/progress_bg.png', 'progress/progress_fg.png')
    self.font = gfw.font.load('neodgm.TTF', 50)
    
    self.bg = gfw.Sprite('tile/Loading.jpg', center_x, center_y)
    world.append(self, 1)
    self.bgi = self.bg.image
    self.image_index = 0
    self.image_count = len(IMAGE_FILES)
    self.images = iter(IMAGE_FILES)
    self.file = ''
    self.progress_y = canvas_height // 3
    self.progress_w = canvas_width * 2 // 3
    self.other_x = center_x - self.progress_w // 2
    self.color = (102, 153, 255)
    self.finish = False

def update():
    if self.finish: return
    self.file = next(self.images, None)
    if self.file is None:
        self.finish = True
        return
    #print(f'Loading {self.file=}')
    gfw.image.load(self.file)
    self.image_index += 1

def draw():
    progress = None
    if self.finish:
        progress = self.image_index / self.image_count
        progress = min(progress, 1)
    else:
        progress = 1
    self.bgi.draw(self.bg.x, self.bg.y, 1280, 1280)
    self.gauge.draw(center_x, self.progress_y, self.progress_w, progress)
    if not self.finish:
        self.font.draw(self.other_x, self.progress_y - 50, self.file, self.color)
    else:
        self.font.draw(center_x - 370 , self.progress_y - 60, "Press any key to continue...", self.color)
    self.font.draw(self.other_x, self.progress_y + 50, '%.1f%%' % (progress * 100), self.color)
    
    
def exit():
    gfw.image.unload('tile/Loading.jpg')
    world.clear()
    del self.font

def handle_event(e):
    if self.finish:
        if e.type == SDL_KEYDOWN:
            gfw.change(menu_scene)
        elif e.type == SDL_MOUSEBUTTONDOWN:
            gfw.change(menu_scene)

IMAGE_FILES = [
    'cards/SkillCardHp.png',
    'cards/SkillCardMaxHp.png',
    'cards/SkillCardSpeed.png',
    'cards/SkillCardAttackSpeed.png',
    'cards/SkillCardRange.png',
    'cards/SkillCardBullet1.png',
    'cards/SkillCardBullet2.png',
    'cards/SkillCardGun.png',
    'cards/SkillCardBase.png',
    'effect/GunEffect.png',
    
    'player/mainC.png',
    
    'prop/Gun.png',
    'prop/Bullet2.png',
    'prop/Bullet2_purple.png',
    'prop/Coin.png',
    'prop/Vaccine.png',
    'prop/Magnetic.png',
    'tile/Tiles.png',
    'tile/Title.jpg',
    
    'ui/Aim.png',
    'ui/Hp.png',
    
    'zombie/zombie1.png',
    'zombie/zombie2.png',
    'zombie/zombie3.png',
    'zombie/zombie4.png',
    'zombie/zombieR.png',
    'zombie/zombieT.png',
]

if __name__ == '__main__':
    gfw.start_main_module()