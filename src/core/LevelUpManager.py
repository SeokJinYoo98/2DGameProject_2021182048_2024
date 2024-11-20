import gfw
import random
from pico2d import *
from cards import *
      
class LevelUpManager:
    def __init__(self):
        self.CARDS = ("H", "MH", "S", "AS", "R", "B1", "B2", "G")
        self.cards = []
        self.__player = gfw.top().world.player
        self.isLevelUp = False
    def handle_event(self, event):
        if not self.isLevelUp: return
        self.__player_input(event)
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
        newCard = self.__choice_card(x, y)
        while any(card.name == newCard.name for card in self.cards):
            newCard = self.__choice_card(x, y)
        self.cards.append(newCard)
        world = gfw.top().world
        world.append(newCard, world.layer.cards)

    def __choice_card(self, x, y):
        newCard = random.choice(self.CARDS)
        if newCard == 'H':
            return HpCard(x, y)
        elif newCard == 'MH':
            return MaxHpCard(x, y)
        elif newCard == 'S':
            return SpeedCard(x, y)
        elif newCard == 'AS':
            return AttackSpeedCard(x, y)
        elif newCard == 'B1':
            return Bullet1Card(x, y)
        elif newCard == 'B2':
            return Bullet2Card(x, y)
        elif newCard == 'R':
            return RangeCard(x, y)
        elif newCard == 'G':
            return GunCard(x, y)
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

    def __player_input(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                self.__player.adjust_delta(-1, 0)
            elif event.key == SDLK_d:
                self.__player.adjust_delta(1, 0)
            elif event.key == SDLK_w:
                self.__player.adjust_delta(0, 1)
            elif event.key == SDLK_s:
                self.__player.adjust_delta(0, -1)
            elif event.key == SDLK_l:
                self.__player.Xp +=1
                
        if event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                self.__player.adjust_delta(1, 0)
            elif event.key == SDLK_d:
                self.__player.adjust_delta(-1, 0)
            elif event.key == SDLK_w:
                self.__player.adjust_delta(0, -1)
            elif event.key == SDLK_s:
                self.__player.adjust_delta(0, 1)