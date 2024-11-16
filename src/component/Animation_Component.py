from component import Component

class Animation_Component(Component):
    def __init__(self):
        self.__frames = {}
        self.__frames_info = {}

        self.__frame_time = 0
        self.__elapsed_time = 0

        self.__frame_count = 0
        self.__frame_index = 0

    def update(self, frame_time):
        self.__elapsed_time += frame_time
        if self.__elapsed_time >= self.__frame_time:
            self.__elapsed_time = 0
            self.__frame_index += 1
            if self.__frame_index >= self.__frame_count:
                self.__frame_index = 0
                
    def get_frame(self, state):
        """Returns the current frame for a given state."""
        if state not in self.__frames:
            return None
        return self.__frames[state][self.__frame_index]
    
    def change_anim_Info(self, state):
        if state not in self.__frames_info: return None
        self.__frame_count = self.__frames_info[state][0]
        self.__frame_time = self.__frames_info[state][1]
        self.__frame_index = 0 
    