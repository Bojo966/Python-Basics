#Изписване на число до 100 с думи

digits = ["zero", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]

teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

decades = ["twenty", "thirty", "forty",
           "fifty", "sixty", "seventy", "eighty", "ninety"]


num = int(input())

firstDigit = (num / 10) * 10
secondDigit = num % 10

if (num < 0 or num > 100):
    print('invalid number')

elif (num <= 9):
    print(digits[num % 10])

elif (num <= 19):
    print(teens[num % 10])

elif (num <= 99 and num % 10 == 0):
    print(decades[int(num / 10) - 2])

elif (num <= 99 and num % 10 != 0):
    print(decades[int(num / 10) - 2] + ' ' + digits[num % 10])

else:
    print("one hundred")