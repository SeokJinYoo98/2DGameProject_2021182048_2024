import gfw
from pico2d import *

class Card(gfw.Sprite):
    Frames = {
        "Non": (0, 0, 48, 62),
        "Click": (49, 0, 48, 62)
    }
    Font = None
    def __init__(self, path, x, y):
        super().__init__(path, x,  y)
        if Card.Font is None:
            Card.Font = gfw.font.load('neodgm.TTF', 32)
            
        self.player = gfw.top().world.player
        self.is_mouse_on = False
        self.height *= 9
        self.width *= 4
        self.text = None
        self.font_offsetX = 20
        self.font_offsetY = -60
    def update(self):
        pass      
    def draw(self):
        frame = Card.Frames["Click"]
        if not self.is_mouse_on: frame = Card.Frames['Non']
        self.image.clip_draw(*frame, self.x, self.y, self.width, self.height)
        gfw.draw_centered_text(Card.Font, self.text, self.x + self.font_offsetX, self.y + self.font_offsetY)
    def _erase(self):
        world = gfw.top().world
        world.remove(self, world.layer.cards)
    def levelUp(self):
        pass
    def is_mouse_in_card(self, mx, my):
        l, b, r, t = self.get_bb()
        if l < mx and mx < r:
            if b <= my and my <= t:
                self.is_mouse_on = True
                return
                
        self.is_mouse_on = False

class HpCard(Card):
    def __init__(self, x, y):
        path = 'cards/SkillCardHp.png'
        super().__init__(path, x, y)
        self.text = "Hp 회복"
    def levelUp(self):
        self.player.hp = self.player.maxHp
        print(f"레벨업{self.player.hp=}")
class MaxHp(Card):
    def __init__(self, x, y):
        path = 'cards/SkillCardMaxHp.png'
        super().__init__(path, x, y)
        self.text = "Max Hp 증가"
    def levelUp(self):
        self.player.maxHp += 1
        print(f"Max레벨업{self.player.maxHp=}")

        
        
class LevelUpManager:
    def __init__(self):
        self.cards = []
        self.__player = gfw.top().world.player
        self.isLevelUp = False

    def handle_event(self, event):
        if not self.isLevelUp: return
        self.__is_mouse_on(event)
        self.__is_clicked(event)

        
    def draw(self):
        pass
    def update(self):
        if self.isLevelUp:
            pass
        else:
            self.__check_level()
    
    def __check_level(self):
        if self.__isLevelUp():
            self.pause()
            self.__player.Xp -=1
            self.__creates_cards()
    
    def __isLevelUp(self):
        if self.__player.Xp >= 1:
            print("LevelUp")
        return self.__player.Xp >= 1
    
    def __creates_cards(self):
        offset = gfw.get_canvas_width() // 3
        x = gfw.get_canvas_width() // 2 - offset
        y = gfw.get_canvas_height() // 2
        for i in range(3):
            self.__creates_card(x, y)
            x += offset
            
    def __creates_card(self, x, y):
        world = gfw.top().world
        card = MaxHp(x, y)
        self.cards.append(card)
        world.append(card, world.layer.cards)
    def __is_mouse_on(self, event):
        if event.type == SDL_MOUSEMOTION:
            mouse_x,  mouse_y = event.x, get_canvas_height() - event.y
            for card in self.cards:
                card.is_mouse_in_card(mouse_x, mouse_y)
    def __is_clicked(self, event):
        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                if self.__clicked_check():
                    self.__clear_cards()
                   
    def __clear_cards(self):
        for card in self.cards:
            card._erase()
        self.cards.clear()
        self.resume()  
              
    def __clicked_check(self):
        for card in self.cards:
            if card.is_mouse_on:
                card.levelUp()
                return True
        return False                   
    def pause(self):
        self.isLevelUp = True
        gfw.top().pause()
    def resume(self):
        self.isLevelUp = False
        gfw.top().resume()