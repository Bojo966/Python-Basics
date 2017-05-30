import math

n = int(input())

isPrime = 1
if n < 2 :
    print('Not Prime')
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            isPrime = 0

    if isPrime:
        print('Prime')
    else:
        print('Not Prime')