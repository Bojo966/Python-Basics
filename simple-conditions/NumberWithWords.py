inputNumber = int(input())

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
lenghtOfNumbers = len(numbers)
if lenghtOfNumbers <= inputNumber:
    print('number too big')
else:
    print(numbers[inputNumber])