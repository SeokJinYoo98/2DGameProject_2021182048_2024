import gfw
from core import Entity
from component import Transform_Component, Movement_Component, HealthComponent

class Player(Entity):
    def __init__(self):
        Info = 'player/mainC.png', gfw.get_canvas_width() / 2, gfw.get_canvas_height() / 2
        super().__init__(*Info)
        self.add_components(Transform_Component, Transform_Component(2, 2))
        self.add_components(Movement_Component, Movement_Component(100, 1))
        self.add_components(HealthComponent, HealthComponent(3))
        
    def update(self):
        h = self.get_component(HealthComponent)
        print(h.get_hp())
        pass
       
    def draw(self):
        current_frame = (0, 0, 18, 20)
        self.image.clip_composite_draw(*current_frame,  0, ' ', self.x, self.y, w=50, h=50)
    
    def get_bb(self):
        l = self.x - self.width // 3
        b = self.y - self.height // 3
        r = self.x + self.width // 3
        t = self.y + self.height // 3
        return l, b, r, t