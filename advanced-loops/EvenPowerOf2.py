import math
n = int(input())

for i in range (n + 1):
    if i % 2 == 0:
        print(int(math.pow(2, i)))