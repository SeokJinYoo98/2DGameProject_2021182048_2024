from component import Component
from gfw import load_data

class Animation_Component(Component):
    def __init__(self, path):
        super().__init__()
        self.__frames = None
        self.__frame_info = None

        self.__frame_time = 0
        self.__elapsed_time = 0

        self.__frame_count = 0
        self.__frame_index = 0
        
        self.__set_anim_info(path)
        
    @property
    def frames(self):
        return self.__frames
    @frames.setter
    def frames(self, frames):
        self.__frames = frames
    @property
    def frame_info(self):
        return self.__frame_info
    @frame_info.setter
    def frame_info(self, frame_info):
        self.__frame_info = frame_info
    
    def update(self, frame_time):
        if self.__frames is None or self.__frame_index is None:
            return
        self.__elapsed_time += frame_time
        if self.__elapsed_time >= self.__frame_time:
            self.__elapsed_time = 0
            self.__frame_index += 1
            if self.__frame_index >= self.__frame_count:
                self.__frame_index = 0
                
    def get_frame(self, state):
        if state not in self.__frames:
            return None
        return self.__frames[state][self.__frame_index]
    
    def change_anim(self, state):
        if not self.__frame_info:
            print("Error: __frames_info가 초기화되지 않았습니다.")
            return None
        if state not in self.__frame_info:
            print(f"Error: {state} 키가 __frames_info에 존재하지 않습니다.")
            return None

        self.__frame_count = self.__frame_info[state][0]
        self.__frame_time = self.__frame_info[state][1]
        self.__frame_index = 0
        
    def __set_anim_info(self, path):
            frames, frame_info = load_data(path)
            self.frames = frames
            self.frame_info = frame_info