numberOfInputNumbers = int(input())
max = int(input())
for i in range(0, numberOfInputNumbers - 1):
    currentNumber = int(input())
    if currentNumber > max:
        max = currentNumber

print(max)