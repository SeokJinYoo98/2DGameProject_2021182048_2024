from pico2d import *
from gfw import gobj
import random as r

class RandomTileBackground(gobj.Sprite):
    def __init__(self, path, tileSize=18, scale=2, margin=0):
        super().__init__(path, 0, 0)
        self._scale = scale
        self._size = tileSize * scale
        self._visible_tiles = {}  # 화면에 보이는 타일을 저장하는 딕셔너리
        
        # 화면 크기 설정
        self.x = get_canvas_width() // 2
        self.y = get_canvas_height() // 2
        
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
       
        if not self._visible_tiles:
            return
        
        for key, (coords, x, y) in self._visible_tiles.items():
            self._Draw_Tile(coords, x, y)

    def update(self):
        pass
    
    def _Get_Random_Tile(self):
        # 무작위로 타일 정보를 선택하여 반환합니다.
        key = r.randint(1, 15)
        if key == 4 or 6 < key:
            key = 4
        return self._tileInfo[key]
    
    def _Generate_Visible_Tiles(self):
        self._visible_tiles.clear()
    
        xCount = math.ceil(get_canvas_width() / self._size)
        yCount = math.ceil(get_canvas_height() / self._size)
        totalCount = xCount * yCount
        print(f"{xCount=}, {yCount=}, {self._size}")
        startX = self.x - math.ceil(get_canvas_width() / 2)
        startY = self.y - math.ceil(get_canvas_height() / 2)
        
        newTile = { }
        key = 0
        for y in range(yCount):
            for x in range(xCount):
                tile = self._Get_Random_Tile()
                posX = startX + x * self._size
                posY = startY + y * self._size
                newTile[key] = (tile['coords'], posX, posY)
                key += 1
                #print(f"{posX=}, {posY}")
        
        self._visible_tiles = newTile
        
        
    def _Draw_Tile(self, coords, x, y):
        drawInfo = *coords, x, y, self._size, self._size
        self.image.clip_draw_to_origin(*drawInfo)
        #self.image.clip_draw(*drawInfo)