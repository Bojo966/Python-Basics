n = int(input())

row = 1
currentNumber = 1
col = 1
while currentNumber <= n:
    currentCol = 0
    while currentNumber <= n and currentCol < col:
        print('{0} '.format(currentNumber), end='')
        currentNumber += 1
        currentCol += 1
    print()
    col += 1