x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
xOfPoint = float(input())
yOfPoint = float(input())

if xOfPoint <= x2 and xOfPoint >= x1 and yOfPoint >= y1 and yOfPoint <= y2:
    print('Inside')
else:
    print('Outside')