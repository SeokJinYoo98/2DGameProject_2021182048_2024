from pico2d import *
from gfw import gobj
import random as r

# Generator와 분리하면 좋을듯.
class RandomTileBackground(gobj.InfiniteScrollBackground):
    def __init__(self, path, tileSize=18, scale=2, margin=0):
        super().__init__(path, margin)
        self.collType = False
        self._scale = scale
        self._size = tileSize * scale
        # 화면에 보이는 타일을 저장하는 딕셔너리
        self._visible_tiles = {}
        self.dx, self.dy = 0, 0
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
    def show(self, x, y):
        prevX, prevY = self.x, self.y
        cw, ch = get_canvas_width(), get_canvas_height()
        if self.margin > 0:
            if x < self.x + self.margin:
                self.x = x - self.margin
            elif x > self.x + cw - self.margin:
                self.x = x - cw + self.margin
            if y < self.y + self.margin:
                self.y = y - self.margin
            elif y > self.y + ch - self.margin:
                self.y = y - ch + self.margin
                
            self.dx += self.x - prevX
            self.dy += self.y - prevY
            return
        self.x = x - cw // 2
        self.y = y - ch // 2
        
    def draw(self):
        width_ = get_canvas_width() // 2
        height_ = get_canvas_height() // 2
        for key, (coords, x, y) in self._visible_tiles.items():
            # 타일 위치 계산
            adjusted_x = x - self.x + width_
            adjusted_y = y - self.y + height_
            
            if -self._size > adjusted_x: continue
            if -self._size > adjusted_y: continue
            if get_canvas_width() < adjusted_x: continue
            if get_canvas_height() < adjusted_y: continue
            
            self._Draw_Tile(coords, adjusted_x, adjusted_y)

    def update(self):
        self._Check_Update_BG()
    
    def _Get_Random_Tile(self):
        key = r.randint(1, 15)
        if 6 < key:
            key = 4
        return self._tileInfo[key]
    
    def _Generate_Visible_Tiles(self):
        self._visible_tiles.clear()
  
        self.xCount = math.ceil((get_canvas_width() * 2) / self._size)
        self.yCount = math.ceil((get_canvas_height() * 2) / self._size)

        startX = self.x - get_canvas_width()
        startY = self.y - get_canvas_height()
        
        newTile = {}
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
        
    def _Check_Update_BG(self):
        dx = math.floor(self.dx)
        dy = math.floor(self.dy)
        
        if dx < -self._size:
            self.dx += self._size
            self._ShiftRight()
        elif dx > self._size:
            self.dx -= self._size
            self._ShiftLeft()
        if dy < -self._size:
            self.dy += self._size
            self._ShiftDown()  
        elif dy > self._size:
            self.dy -= self._size
            self._ShiftUp()
        
    def _ShiftLeft(self):
        newTile = { }
        for key, (coords, x, y) in self._visible_tiles.items():
            # 새타일을 만든다.
            if (key + 1) % self.yCount == 0:
                tile = self._Get_Random_Tile()
                posX = self._visible_tiles[key][1] + self._size
                posY = self._visible_tiles[key][2]
                newTile[key] = (tile['coords'], posX, posY)
            else:
                # Shift
                newTile[key] = self._visible_tiles[key + 1]
        self._visible_tiles.clear()
        self._visible_tiles = newTile

    def _ShiftRight(self):
        newTile = { }
        for key, (coords, x, y) in self._visible_tiles.items():
            # 타일 생성
            if key % self.yCount == 0:
                tile = self._Get_Random_Tile()
                posX = self._visible_tiles[key][1] - self._size
                posY = self._visible_tiles[key][2]
                newTile[key] = (tile['coords'], posX, posY)
            else:
                # Shift
                newTile[key] = self._visible_tiles[key - 1]
        self._visible_tiles.clear()
        self._visible_tiles = newTile
    
    def _ShiftDown(self):
        newTile = {}
        for key, (coords, x, y) in self._visible_tiles.items():
            if key < self.xCount:
                tile = self._Get_Random_Tile()
                posX = self._visible_tiles[key][1]
                posY = self._visible_tiles[key][2] - self._size
                newTile[key] = (tile['coords'], posX, posY)
            else:
                newTile[key] = self._visible_tiles[key - self.xCount]
        self._visible_tiles.clear()
        self._visible_tiles = newTile
                
    def _ShiftUp(self):
        newTile = {}
        for key, (coords, x, y) in self._visible_tiles.items():
            maxIndex = self.xCount * self.yCount - 1
            startIndex = maxIndex - self.xCount
            if key >= startIndex:
                tile = self._Get_Random_Tile()
                posX = self._visible_tiles[key][1]
                posY = self._visible_tiles[key][2] + self._size
                newTile[key] = (tile['coords'], posX, posY)
            else:
                newTile[key] = self._visible_tiles[key + self.xCount]
        self._visible_tiles.clear()
        self._visible_tiles = newTile