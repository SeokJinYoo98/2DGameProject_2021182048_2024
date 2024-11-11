from items import *
import gfw
import random

def CreateItem(x, y):
    randIndex = random.randint(0, 10)
    newItem = None
    if randIndex == 0:
        newItem = Vaccine(x, y)
    else:
        newItem = Coin(x, y)
        
    world = gfw.top().world
    
    world.append(newItem, world.layer.item)
        