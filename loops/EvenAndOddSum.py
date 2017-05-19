numbersToRead = int(input())

evenSum = 0
oddSum = 0

for i in range(0, numbersToRead):
    currentNumber = int(input())
    if i % 2 == 0:
        evenSum += currentNumber
    else:
        oddSum += currentNumber

if oddSum == evenSum:
    print('Yes')
    print('Sum = {0}'.format(oddSum))
else:
    print('No')
    print('Diff = {0}'.format(abs(oddSum - evenSum)))

