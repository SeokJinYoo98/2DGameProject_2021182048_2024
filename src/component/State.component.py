from component import Component

class State_Component(Component):
    def __init__(self, anim_comp=None):
        self.__state = 'IDLE'
        self.__anim = anim_comp
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_state):
        if self.__state != 'DEAD':
            self.__state = new_state
            if self.__anim:
                self.__anim.change_anim(self.__state)
                
