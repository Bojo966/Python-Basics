firstInterval = int(input())
secondInterval = int(input())
thirdInterval = int(input())

totalSeconds = firstInterval + secondInterval + thirdInterval
minutes = int(totalSeconds / 60)
restOfSeconds = totalSeconds % 60

print('{0}:{1}'.format(minutes, str(restOfSeconds).zfill(2)))