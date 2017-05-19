movieType = input()
numberOfRows = int(input())
numberOfCols = int(input())

if movieType == 'Premiere':
    ticketPrice = 12
elif movieType == 'Normal':
    ticketPrice = 7.5
else:
    ticketPrice = 5

print('{0:.2f} leva'.format(numberOfCols * numberOfRows * ticketPrice))