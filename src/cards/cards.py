import gfw

class Card(gfw.Sprite):
    Frames = {
        "Non": (0, 0, 48, 62),
        "Click": (49, 0, 48, 62)
    }
    Font = None
    def __init__(self, path, x, y):
        super().__init__(path, x,  y)
        if Card.Font is None:
            Card.Font = gfw.font.load('neodgm.TTF', 28)
        self.__sfx = gfw.sfx('Select.wav')
        self.__sfx.set_volume(50)
        self.player = gfw.top().world.player
        self.is_mouse_on = False
        self.height *= 7
        self.width *= 3.3
        self.name = None
        self.explanation = None
        self.font_offsetX = 20
        self.font_offsetY = 0
    def update(self):
        pass      
    def draw(self):
        frame = Card.Frames["Click"]
        if not self.is_mouse_on: frame = Card.Frames['Non']
        self.image.clip_draw(*frame, self.x, self.y, self.width, self.height)
        gfw.draw_centered_text(Card.Font, self.name, self.x + self.font_offsetX - 20, self.y + self.font_offsetY)
        gfw.draw_centered_text(Card.Font, self.explanation, self.x + self.font_offsetX, self.y + self.font_offsetY - 60)
    def _erase(self):
        world = gfw.top().world
        world.remove(self, world.layer.cards)
    def levelUp(self):
        pass
    def is_mouse_in_card(self, mx, my):
        l, b, r, t = self.get_bb()
        if l < mx and mx < r:
            if b <= my and my <= t:
                if not self.is_mouse_on:
                    self.__sfx.play()
                    self.is_mouse_on = True
                return
        self.is_mouse_on = False
class HpCard(Card):
    def __init__(self, x, y):
        path = 'cards/SkillCardHp.png'
        super().__init__(path, x, y)
        self.name = "[Divine Grace]"
        self.explanation = "Hp 회복"
    def levelUp(self):
        self.player.hp = self.player.maxHp

class MaxHpCard(Card):
    def __init__(self, x, y):
        path = 'cards/SkillCardMaxHp.png'
        super().__init__(path, x, y)
        self.name = "[Divine Blessing]"
        self.explanation = " 최대 Hp 증가"
    def levelUp(self):
        self.player.maxHp += 1

class SpeedCard(Card):
    def __init__(self, x, y):
        path = 'cards/SkillCardSpeed.png'
        super().__init__(path, x, y)
        self.name = "[Adrenaline]"
        self.explanation = "    이동속도 증가"
    def levelUp(self):
        self.player.speed += 5

class AttackSpeedCard(Card):
    def __init__(self, x, y):     
        path = 'cards/SkillCardAttackSpeed.png'
        super().__init__(path, x, y)
        self.name = "[Stimpack]"
        self.explanation = "    공격속도 증가"
    def levelUp(self):
        self.player.bullet_Cooltime -= 0.008

class RangeCard(Card):
    def __init__(self, x, y):     
        path = 'cards/SkillCardRange.png'
        super().__init__(path, x, y)
        self.name = "[Scope]"
        self.explanation = "    공격 사거리 증가"
    def levelUp(self):
        self.player.bullet_Range += 50

class Bullet1Card(Card):
    def __init__(self, x, y):     
        path = 'cards/SkillCardBullet1.png'
        super().__init__(path, x, y)
        self.name = "[Barrel]"
        self.explanation = "   탄환 개수 증가"
    def levelUp(self):
        self.player.bullet_RowCnt += 1
 
class Bullet2Card(Card):
    def __init__(self, x, y):     
        path = 'cards/SkillCardBullet2.png'
        super().__init__(path, x, y)
        self.name = "[Bullet]"
        self.explanation = "   탄환 관통 증가"
    def levelUp(self):
        self.player.bullet_Penetration += 1

class GunCard(Card):
    def __init__(self, x, y):     
        path = 'cards/SkillCardGun.png'
        super().__init__(path, x, y)
        self.name = "[Gun]"
        self.explanation = "    연속 발사 증가"
    def levelUp(self):
        self.player.bullet_ColCnt += 1
