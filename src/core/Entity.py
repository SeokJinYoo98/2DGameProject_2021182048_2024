import gfw
from component import *
class Entity(gfw.Sprite):
    def __init__(self, path, x, y):
        super().__init__(path, x, y)
        self.__components = {}
    @property
    def components(self):
        return self.__components
    
    def update(self):
        pass
                  
    def handle_event(self, e):
        pass
    
    def draw(self):
        if self.components[Animation_Component]:
            self.clip_draw()
            
    def addDir(self, dx, dy):
        mv = self.components[Movement_Component]
        if not mv: return
        self.components[Movement_Component].direction(dx, dy)    
                       
    def add_components(self, component_Type=None, component=None):
        if component_Type is None: return
        if component_Type in self.__components: return
        self.__components[component_Type] = component
        component.entity = self
                
    def get_bb(self):
        if self.collType is False: return None
        scale = self.components[Transform_Component].scale
        l = self.x - self.width // 2
        b = self.y - self.height // 2
        r = self.x + self.width // 2
        t = self.y + self.height // 2
        return l, b, r, t
    def get_comp(self, type):
        return self.components[type] 
    
    def clip_draw(self):
        state = self.__components[State_Component].state
        current_frame = self.__components[Animation_Component].get_frame(state)
        rt = self.__components[Transform_Component].rotation
        flip = self.__components[Movement_Component].flip
        pos = self.x, self.y
        scale = self.__components[Transform_Component].scale
        sc = self.width * scale[0], self.height * scale[1] 
        self.image.clip_composite_draw(*current_frame, rt, flip, *pos, *sc)
    
    def __get_clip_info(self):
        state = self.__components[State_Component].state
        current_frame = self.__components[Animation_Component].get_frame(state)
        rt = self.__components[Transform_Component].rotation
        flip = self.__components[Movement_Component].flip
        pos = self.x, self.y
        scale = self.__components[Transform_Component].scale
        sc = self.width * scale[0], self.height * scale[1] 
        return [*current_frame, rt, flip, *pos, *sc]
        
    def _apply_movement(self):
        tr = self.get_comp(Transform_Component)
        mv = self.get_comp(Movement_Component)
        if not tr or not mv: return
        x = mv.get_movementX() * gfw.frame_time
        y = mv.get_movementY() * gfw.frame_time
        tr.add_translate(x, y)
    
    def _apply_animation(self):
        anim_comp = self.get_comp(Animation_Component)
        if not anim_comp: return
        anim_comp.update(gfw.frame_time)
        
 
    