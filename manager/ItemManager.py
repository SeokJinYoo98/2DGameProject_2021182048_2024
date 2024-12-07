from items import *
import gfw
import random

# 클래스로 작성하고, 아이템의 기능을 담당하게
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
        