import math
figure = input()

if figure == 'square':
    side = float(input())
    print('{0:.3f}'.format(side * side))
elif figure == 'rectangle':
    sideA = float(input())
    sideB = float(input())
    print('{0:.3f}'.format(sideA * sideB))
elif figure == 'circle':
    radius = float(input())
    print('{0:.3f}'.format(radius * math.pi * radius))
else:
    side = float(input())
    height = float(input())
    print('{0:.3f}'.format(side * height / 2))