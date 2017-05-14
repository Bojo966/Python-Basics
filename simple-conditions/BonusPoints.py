inputNumber = int(input())

if inputNumber <= 100:
    bonusPoints = 5
elif inputNumber <= 1000:
    bonusPoints = inputNumber * 0.2
else:
    bonusPoints = inputNumber * 0.1

if inputNumber % 2 == 0:
    bonusPoints += 1
elif inputNumber % 10 == 5:
    bonusPoints += 2

print(bonusPoints)
print(inputNumber + bonusPoints)