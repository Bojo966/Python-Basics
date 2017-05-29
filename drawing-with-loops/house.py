n =  int(input())
if n % 2 == 0:
    startRoofStars = 2
else:
    startRoofStars = 1

for i in range(0, int((n + 1) / 2)):
    undescores = int((n - startRoofStars) / 2)
    print('-' * undescores + '*' * startRoofStars + '-' * undescores)
    startRoofStars += 2

for i in range(0, int(n / 2)):
    print('|' + '*' * (n - 2) + '|')