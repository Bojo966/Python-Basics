numbersToRead = int(input())
leftSum = 0
rightSum = 0

for i in range(0, numbersToRead):
    currentNumber = int(input())
    leftSum += currentNumber

for i in range(0, numbersToRead):
    currentNumber = int(input())
    rightSum += currentNumber

if leftSum == rightSum:
    print('Yes, sum = {0}'.format(leftSum))
else:
    diff = abs(leftSum - rightSum)
    print('No, diff = {0}'.format(diff))