n = int(input())


if n % 2 == 0:
    starsForStratAndEnd = 2
else:
    starsForStratAndEnd = 1

underscores = int((n - starsForStratAndEnd) / 2)
print('-' * underscores + '*' * starsForStratAndEnd + '-' * underscores)

for i in range(0, int((n-1)/2)):
    middleUndescores = i * 2 + 1
    if n % 2 == 0 :
        middleUndescores += 1
    endUndescores = int((n - 2 - middleUndescores) / 2)
    print('-' * endUndescores + '*' + '-' * middleUndescores + '*' + '-' * endUndescores)

for i in range(1, int((n-1)/2)):
    middleUndescores = int((n - 2 - i * 2))
    print('-' * i + '*' + '-' * middleUndescores + '*' + '-' * i)

if n > 2 :
    underscores = int((n - starsForStratAndEnd) / 2)
    print('-' * underscores + '*' * starsForStratAndEnd + '-' * underscores)