import math


selector = ".dial span"
l = 6.45
for i in range(1, 13):
    a = math.radians((i - 3) * 30)
    x = math.cos(a) * l
    y = math.sin(a) * l
    print("{}:nth-child({}) {{ transform: translate({:.2f}em, {:.2f}em); }}".format(
        selector, i, x, y
    ))
