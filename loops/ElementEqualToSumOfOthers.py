n = int(input())
max = int(input())
sum = max
for i in range(n - 1):
    tmp = int(input())
    if tmp > max:
        max = tmp
    sum += tmp
if sum - max == max:
    print("Yes\nSum =", sum - max)
else:
    print("No\nDiff =", abs(sum - max - max))
