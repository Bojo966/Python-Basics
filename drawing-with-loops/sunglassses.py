n = int(input())

width = n * 5
height = n

print('*' * (n * 2) + ' ' * n + '*' * (n * 2))

for i in range(1, n-1):
    if i == int((n-1) / 2):
        print('*' + '/' * (n * 2 - 2) + '*' + '|' * n + '*' + '/' * (n * 2 - 2) + '*')
    else:
        print('*' + '/' * (n * 2 - 2) + '*' + ' ' * n + '*' + '/' * (n * 2 - 2) + '*')

print('*' * (n * 2) + ' ' * n + '*' * (n * 2))
