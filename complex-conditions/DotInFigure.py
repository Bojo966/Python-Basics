h = int(input())
x = int(input())
y = int(input())
if ((x < h and y > h) or (x > 2 * h and y > h) or (x < 0) or (x > 3 * h) or (y < 0) or (y > 4 * h)):
    print("outside")
elif ((x > 0 and x < 3 * h and y > 0 and y < h) or (x > h and x < 2 * h and y < 4 * h and y > 0)):
    print("inside")
else:
    print("border")