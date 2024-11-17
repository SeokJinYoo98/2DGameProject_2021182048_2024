import math

def get_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx ** 2 + dy ** 2)

def get_direction(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx ** 2 + dy ** 2)
    if distance > 0:
        return dx / distance, dy / distance
    return 0, 0

def get_radian(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    return math.atan2(dy, dx)