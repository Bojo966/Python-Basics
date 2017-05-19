n = int(input())
oddSum = 0.0
oddMin = 1000000000
oddMax = -1000000000
evenSum = 0.0
evenMin = 1000000000
evenMax = -1000000000
for i in range(1, n + 1):
    temp = float(input())
    if i % 2 == 0:
        evenSum += temp
        if evenMax < temp:
            evenMax = temp
        if evenMin > temp:
            evenMin = temp
    else:
        oddSum += temp
        if oddMax < temp:
            oddMax = temp
        if oddMin > temp:
            oddMin = temp
print("OddSum=" + str(oddSum) + ',')
if oddMin == 1000000000:
    print("OddMin=No,")
else:
    print("OddMin=" + str(oddMin) + ',')
if oddMax == -1000000000:
    print("OddMax=No,")
else:
    print("oddMax=" + str(oddMax  ) + ',')
print("EvenSum=" + str(evenSum) + ',')
if evenMin == 1000000000:
    print("EvenMin=No,")
else:
    print("EvenMin=" + str(evenMin) + ',')
if evenMax == -1000000000:
    print("EvenMax=No,")
else:
    print("EvenMax=" + str(evenMax  ) + ',')