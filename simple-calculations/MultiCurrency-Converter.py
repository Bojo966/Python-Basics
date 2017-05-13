quanitity = float(input())
inputCurrency = input()
outputCurrency = input()

usdFactor = 1.79549
eurFactor = 1.95583
gbpFactor = 2.53405

if inputCurrency == 'USD':
    levas = quanitity * usdFactor
elif inputCurrency == 'EUR':
    levas = quanitity * eurFactor
elif inputCurrency == 'GBP':
    levas = quanitity * gbpFactor
elif inputCurrency == 'BGN':
    levas = quanitity

if outputCurrency == 'USD':
    outputQuantity = levas / usdFactor
elif outputCurrency == 'EUR':
    outputQuantity = levas / eurFactor
elif outputCurrency == 'GBP':
    outputQuantity = levas / gbpFactor
elif outputCurrency == 'BGN':
    outputQuantity = levas

print('{0:.2f}'.format(outputQuantity))

