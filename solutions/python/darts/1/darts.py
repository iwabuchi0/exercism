import math
def score(x, y):
    distancia = math.hypot(x,y)
    if distancia <= 1:
        return 10
    if distancia <= 5:
        return 5
    if distancia <=10:
        return 1
    return 0


