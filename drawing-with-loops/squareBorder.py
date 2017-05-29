n = int(input())

print('+ ' + str('- ' * (n -2)) + '+')

for i in range(0, n - 2):
    print('| ' + str('- ' * (n - 2)) + '|')

print('+ ' + str('- ' * (n -2)) + '+')
