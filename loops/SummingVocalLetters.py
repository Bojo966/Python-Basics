word = input()
vocals = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
sum = 0

for i in word:
    if i in vocals.keys():
        sum += vocals[i.lower()]

print(sum)