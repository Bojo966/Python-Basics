inputVelocity = float(input())

if  inputVelocity <= 10:
    print('slow')
elif inputVelocity <= 50:
    print('average')
elif inputVelocity <= 150:
    print('fast')
elif inputVelocity <= 1000:
    print('ultra fast')
else:
    print('extremely fast')