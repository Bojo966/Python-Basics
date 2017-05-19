inputNumber = float(input())

inRange = inputNumber >= 100 and inputNumber <= 200 or inputNumber == 0

if not inRange:
    print('invalid')