import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

width = math.fabs(x2 - x1)
height = math.fabs(y2 - y1)

print(width * height)
print((width + height) * 2 )