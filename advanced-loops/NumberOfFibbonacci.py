previousNumber = 1
currentNumber = 1

n = int(input())

if n < 2:
    print(1)
else:
    for i in range (0, n - 1):
        nextNumber = previousNumber + currentNumber
        previousNumber = currentNumber
        currentNumber = nextNumber
    print(currentNumber)