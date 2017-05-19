x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

xOfPoint = float(input())
yOfPoint = float(input())


onLeftSide = xOfPoint == x1 and yOfPoint >= y1 and yOfPoint <= y2
onRightSide = xOfPoint == x2 and yOfPoint >= y1 and yOfPoint <= y2
onTopSide = yOfPoint == y1 and xOfPoint >= x1 and xOfPoint <= x2
onBottomSide = yOfPoint == y2 and xOfPoint >= x1 and xOfPoint <= x2

if onTopSide or onBottomSide or onRightSide or onLeftSide:
    print('Border')
else:
    print('Inside / Outside')