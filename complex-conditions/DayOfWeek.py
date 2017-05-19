days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

dayNumber = int(input())

if dayNumber < 1 or dayNumber > 7:
    print('Error')
else:
    print(days[dayNumber - 1])