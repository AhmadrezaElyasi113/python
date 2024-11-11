import math
a = 1
b = -3
c = 2

dicriminant = b*b - 4.0*a*c
if dicriminant < 0:
    print('no real roots')
else:
    d = math.sqrt(dicriminant)
    print((-b + d) / 2.0)
    print((-b - d) / 2.0)