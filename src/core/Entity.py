import gfw
class Entity(gfw.Sprite):
    def __init__(self, path, x, y):
        super().__init__(path, x, y)
        self.__components = {}
    
    def add_components(self, component_Type=None, component=None):
        if component_Type is None: return
        if component_Type in self.__components: return
        self.__components[component_Type] = component
        component.entity = self
        
    def get_component(self, component_type):
        return self.__components.get(component_type, None)

class PlayerController:
    def __init__(self):
        pass

class Aim(Entity):
    def __init__(self):
        pass
class Gun(Entity):
    def __init__(self):
        pass

class ZombieManager:
    def __init__(self):
        pass
    
class Zombie(Entity):
    def __init__(self):
        pass
class ZombieD(Zombie):
    def __init__(self):
        pass
class ZombieR(Zombie):
    def __init__(self):
        pass
class ZombieT(Zombie):
    def __init__(self):
        pass
    
class ItemManager:
    def __init__(self):
        pass
class Item(Entity):
    def __init__(self):
        pass
class Vaccine(Item):
    def __init__(self):
        pass
class Coin(Item):
    def __init__(self):
        pass
    