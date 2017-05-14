hours = int(input())
minutes = int(input())

minutes += 15

hours += int(minutes / 60)
minutes %= 60
hours %= 24

print('{0}:{1}'.format(hours, str(minutes).zfill(2)))