city = input().lower()
amountOfMoney = float(input())

firstRangeCityPercents = { 'sofia': 0.05, 'varna': 0.045, 'plovdiv': 0.055}
secondRangeCityPercents = { 'sofia': 0.07, 'varna': 0.075, 'plovdiv': 0.08}
thirdRangeCityPercents = { 'sofia': 0.08, 'varna': 0.1, 'plovdiv': 0.12}
forthRangeCityPercents = { 'sofia': 0.12, 'varna': 0.13, 'plovdiv': 0.145}

isInCityPercents = city in firstRangeCityPercents.keys()
if isInCityPercents:
    if amountOfMoney < 0:
        print('error')
    elif amountOfMoney <= 500:
        print('{0:.2f}'.format(amountOfMoney * firstRangeCityPercents[city]))
    elif amountOfMoney <= 1000:
        print('{0:.2f}'.format(amountOfMoney * secondRangeCityPercents[city]))
    elif amountOfMoney <= 10000:
        print('{0:.2f}'.format(amountOfMoney * thirdRangeCityPercents[city]))
    else:
        print('{0:.2f}'.format(amountOfMoney * forthRangeCityPercents[city]))
else:
    print('error')
