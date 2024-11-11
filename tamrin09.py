import sys

epsilon = 1e-15

c = 4
t = c
while abs(t - c/t) > (epsilon * t):
    t = (c/t + t) / 2
print(t)