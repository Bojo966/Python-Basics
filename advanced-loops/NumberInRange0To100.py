print('Еnter a number in the range [1...100]: ', end='')
number = int(input())

while number < 1 or number > 100:
    print('Invalid number!')
    print('Еnter a number in the range [1...100]: ', end='')
    number = int(input())

print('The number is: {0}'.format(number))