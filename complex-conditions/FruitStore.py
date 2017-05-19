fruit = input().lower()
dayOfWeek = input().lower()
quantity = float(input())

fruitsInWeekend = {'banana': 2.7, 'apple': 1.25, 'orange': 0.9, 'grapefruit': 1.6, 'kiwi': 3, 'pineapple': 5.6, 'grapes': 4.2}
fruitsInWeekdays = {'banana': 2.5, 'apple': 1.2, 'orange': 0.85, 'grapefruit': 1.45, 'kiwi': 2.7, 'pineapple': 5.50, 'grapes': 3.85}
daysInWeekdays = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
daysInWeekends = {'saturday', 'sunday'}

existingFruit = fruit in fruitsInWeekdays.keys()
existingDay =  dayOfWeek in daysInWeekdays
existingDay = existingDay or (dayOfWeek in daysInWeekends)

if existingFruit and existingDay:
    if dayOfWeek == 'sunday' or dayOfWeek == 'saturday':
        print('{0:.2f}'.format(quantity * fruitsInWeekend[fruit]))
    else :
        print('{0:.2f}'.format(quantity * fruitsInWeekdays[fruit]))
else:
    print('Error')