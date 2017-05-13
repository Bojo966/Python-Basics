size = int(input())
row = ''
for i in range(0, size):
    row += '*'
print(row)


row = ''
for i in range(0, size - 2):
    row = '*'
    for space in range(0, size - 2):
        row += ' '
    row += '*'
    print(row)

row = ''
for i in range(0, size):
    row += '*'
print(row)
