from items import *
import gfw
import random

def CreateItem(x, y):
    randIndex = random.randint(1, 100)
    newItem = None
    if 41 <= randIndex and randIndex <= 45:
        newItem = Vaccine(x, y)
    elif randIndex == 50:
       newItem = Magnetic(x, y)
    else: 
        newItem = Coin(x, y)
        

    world = gfw.top().world
    
    world.append(newItem, world.layer.item)
        