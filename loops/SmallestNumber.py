numberOfInputNumbers = int(input())
min = int(input())
for i in range(0, numberOfInputNumbers - 1):
    currentNumber = int(input())
    if currentNumber < min:
        min = currentNumber

print(min)