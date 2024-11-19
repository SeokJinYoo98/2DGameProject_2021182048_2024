import gfw
from sdl2 import *
from core import Entity
from component import *
class Player_Controller_main:
    def __init__(self):
        self.__player = gfw.top().world.player
        self.__aim = Aim()
        self.DIRECTION_MAP = {
            SDLK_a: (-1, 0),
            SDLK_d: (1, 0),
            SDLK_w: (0, 1),
            SDLK_s: (0, -1)
        }
        self.target = None
        self.__append()
        
    def __append(self):
        world = gfw.top().world
        world.append(self.__aim, world.layer.ui)
        
    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            mouse_x,  mouse_y = event.x, gfw.get_canvas_height() - event.y
            self.__aim.move_to_mouse(mouse_x, mouse_y)
            
        if event.type in (SDL_KEYDOWN, SDL_KEYUP):
            dir = self.DIRECTION_MAP.get(event.key)
            if dir is None: return
            if event.type == SDL_KEYUP: 
                dir = (-dir[0], -dir[1])
            self.__apply_dir(self.__player, dir)
                
    def __apply_dir(self, target, dir):
        target.add_dir(*dir)
        
class Player(Entity):
    def __init__(self):
        Info = 'player/mainC.png', gfw.get_canvas_width() / 2, gfw.get_canvas_height() / 2
        super().__init__(*Info)
        self.add_components(Transform_Component, Transform_Component(0, 1.2, 1.2))
        self.add_components(Movement_Component, Movement_Component(100, 1))
        self.add_components(Health_Component, Health_Component(3))
        self.add_components(Animation_Component, Animation_Component('playerData.json'))
        self.add_components(State_Component, State_Component())
        
    def update(self):
        self._apply_movement()
        self.__check_state()
        self._apply_animation()
    def add_dir(self, dx, dy):
        mv_comp = self.get_comp(Movement_Component)
        if not mv_comp: return
        mv_comp.add_dir(dx, dy)
    def set_target(self, aim):
        self.target = aim    
    def __Fire(self):
        pass
    
    def __check_state(self):
        if self.__is_dead(): self.__do_state('DEAD')
        elif self.__is_move():
            if self.__is_back(): self.__do_state('BACK')
            else: self.__do_state('WALK')
        else: self.__do_state('IDLE')
    def __do_state(self, state_):
        state_comp = self.get_comp(State_Component)
        if not state_comp or state_comp.state == state_: return
        state_comp.state = state_
        anim_comp = self.get_comp(Animation_Component)
        if anim_comp: anim_comp.change_anim(state_comp.state)
    def __is_dead(self):
        hp_comp = self.get_comp(Health_Component)
        if not hp_comp: return None
        return hp_comp.get_hp() <= 0
    def __is_move(self):
        mv_comp = self.get_comp(Movement_Component)
        if not mv_comp: return None
        dir = mv_comp.direction
        return abs(dir[0]) + abs(dir[1]) > 0
    def __is_back(self):
        mv_comp = self.get_comp(Movement_Component)
        if not mv_comp: return None
        if mv_comp.flip == ' ':
            return mv_comp.direction[0] < 0
        else:
            return mv_comp.direction[0] > 0

        
class Bullet(Entity):
    def __init__(self, x, y):
        Info = 'player/mainC.png', x, y
class Aim(Entity):
    def __init__(self):
        Info = 'ui/Aim.png', 0, 0
        super().__init__(*Info)
        self.collType = False
        
    def draw(self):
        self.image.draw(self.x, self.y, 50, 50)
        
    def move_to_mouse(self, mx, my):
        self.x, self.y = mx, my
        
if __name__ == '__main__':
    Player()