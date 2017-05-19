n = int(input())
if n > 1:
    prev = int(input()) + int(input())
    max = -1000000000000000000
    for i in range(n - 1):
        sum = int(input()) + int(input())
        if max < abs(sum - prev):
            max = abs(sum - prev)
        prev = sum
    if max == 0:
        print("Yes, value=" + str(prev))
    else:
        print("No, maxdiff=" + str(max))
else:
    print("Yes, value=" + str(int(input()) + int(input())))
