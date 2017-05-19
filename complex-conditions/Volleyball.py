import math

typeOfYear = input()
numberOfHolidays = float(input())
numberOfWeekedsInHometown = float(input())

numberOfWeekendsAtWorktown = 48 - numberOfWeekedsInHometown
gamesInWorktown = numberOfWeekendsAtWorktown * 3 / 4
gamesInHometown = numberOfWeekedsInHometown
gamesInHolidays = numberOfHolidays * 2 / 3

totalGames = gamesInHolidays + gamesInHometown + gamesInWorktown

if typeOfYear == 'leap':
    totalGames *= 1.15

print(math.floor(totalGames))
