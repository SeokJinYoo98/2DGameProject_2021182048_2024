from sdl2 import *
from component import Component, Movement_Component, State_Component

class Input_Component(Component):
    def __init__(self):
        super().__init__()
        
        self.DIRECTION_MAP = {
        SDLK_LEFT: (-1, 0),
        SDLK_RIGHT: (1, 0),
        SDLK_UP: (0, 1),
        SDLK_DOWN: (0, -1)
        }

    
        