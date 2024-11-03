from pico2d import *
from gfw import gobj
import random as r

class RandomTileBackground(gobj.InfiniteScrollBackground):
    def __init__(self, path, tileSize=18, scale=2, margin=0):
        super().__init__(path, margin=300)
        self._scale = scale
        self._size = tileSize * scale
        self._visible_tiles = {}  # 화면에 보이는 타일을 저장하는 딕셔너리
        
        # 타일 정보 설정
        self._tileInfo = {
            1: {'coords': [0, 0, 18, 18], 'walkable': True},
            2: {'coords': [19, 0, 18, 18], 'walkable': True},
            3: {'coords': [38, 0, 18, 18], 'walkable': True},
            4: {'coords': [0, 19, 18, 18], 'walkable': True},
            5: {'coords': [19, 19, 18, 18], 'walkable': True},
            6: {'coords': [38, 19, 18, 18], 'walkable': False}
        }

        # 초기 보이는 타일들 생성
        self._Generate_Visible_Tiles()
    
    def draw(self):
        for key, (coords, x, y) in self._visible_tiles.items():
            # 타일 위치 계산
            adjusted_x = x - self.x + get_canvas_width() // 2
            adjusted_y = y - self.y + get_canvas_height() // 2
            
            if -self._size > adjusted_x or -self._size > adjusted_y: continue
            if get_canvas_width() < adjusted_x or get_canvas_height() < adjusted_y: continue
            
            self._Draw_Tile(coords, adjusted_x, adjusted_y)

    def update(self):
        dx = math.floor(self.x)
        dy = math.floor(self.y)
        print(f"{dx=},{dy=}")
    
    def _Get_Random_Tile(self):
        key = r.randint(1, 15)
        if 6 < key:
            key = 4
        return self._tileInfo[key]
    
    def _Generate_Visible_Tiles(self):
        self._visible_tiles.clear()
    
        self.xCount = math.ceil((get_canvas_height() * 2) / self._size)
        self.yCount = math.ceil((get_canvas_width() * 2) / self._size)
        totalCount = self.xCount * self.yCount
        
        startX = self.x - math.ceil((get_canvas_height() * 2) / 2)
        startY = self.y - math.ceil((get_canvas_width() * 2) / 2)
        
        newTile = { }
        key = 0
        for y in range(self.yCount):
            for x in range(self.xCount):
                tile = self._Get_Random_Tile()
                posX = startX + x * self._size
                posY = startY + y * self._size
                newTile[key] = (tile['coords'], posX, posY)
                key += 1
                
        self._visible_tiles = newTile
        
    def _Draw_Tile(self, coords, x, y):
        drawInfo = *coords, x, y, self._size, self._size
        self.image.clip_draw_to_origin(*drawInfo)
        #self.image.clip_draw(*drawInfo)
        
    def _Check_Update_BG(self, x, y):
        #print(f"{x=}, {y=}")
        pass
    def _Shift_X(self, min_max):
        pass
            
    def _Change_Y(self, min_max):
        pass
    
    def _findMax_X(self, key):
        return (key + 1) % self.xCount
    def _findMin_X(self, key):
        return key % self.xCount
    