from component import Component, Animation_Component, Health_Component, Movement_Component

class State_Component(Component):
    def __init__(self):
        super().__init__()
        self.__state = 'IDLE'
        
    @property
    def state(self):
        return self.__state
    def update(self):
        pass
    
    @state.setter
    def state(self, new_state):
        if self.__state != 'DEAD':
            self.__state = new_state

        