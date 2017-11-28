import numpy as np
import math
from scipy.spatial import distance

def collision(pin, ball):
    diff = np.subtract(pin.getPosition(), ball.getPosition())
    diff[:] = [i - ball.getRadius() for i in diff]
    length = distance.euclidean((0,0,0), diff)

    pinX = math.degrees(math.cos(pin.getAngles()[0]))*length
    pinY = math.degrees(math.sin(pin.getAngles()[1]))*length
    pinZ = math.degrees(math.sin(pin.getAngles()[1]))*length


'''#Definition refers to the parameters needed to define the pin. [a, b, c] -> ax^2 + by^2 + cz^2 = 1
#Reqirements for this to work:
#Must be able to get a, b, c from pin, origin of pin, point comparing to
from scipy.spatial import distance
import numpy as np

def collision(point, pinCenter):
    diff = np.subtract(pinCenter, point)
    print diff
    a = 1
    b = 1
    c = 1
    if (diff[0]2 / a2) + (diff[1]2 / b2) + (diff[2]2 / c2) > 1:
        return false
    else:
        return true
    #dist = distance.euclidean(point, pinCenter)


collision((1, 2, 3), (1, 2, 4))'''
