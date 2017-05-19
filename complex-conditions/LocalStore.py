product = input().lower()
town = input().lower()
quantity = float(input())

if product == 'coffee':
    if town == 'sofia':
        print('{0:.2f}'.format(quantity * 0.5))
    elif town == 'plovdiv':
        print('{0:.2f}'.format(quantity * 0.4))
    elif town == 'varna':
        print('{0:.2f}'.format(quantity * 0.45))
elif product == 'water':
    if town == 'sofia':
        print('{0:.2f}'.format(quantity * 0.8))
    elif town == 'plovdiv':
        print('{0:.2f}'.format(quantity * 0.7))
    elif town == 'varna':
        print('{0:.2f}'.format(quantity * 0.7))
elif product == 'beer':
    if town == 'sofia':
        print('{0:.2f}'.format(quantity * 1.2))
    elif town == 'plovdiv':
        print('{0:.2f}'.format(quantity * 1.15))
    elif town == 'varna':
        print('{0:.2f}'.format(quantity * 1.1))
elif product == 'sweets':
    if town == 'sofia':
        print('{0:.2f}'.format(quantity * 1.45))
    elif town == 'plovdiv':
        print('{0:.2f}'.format(quantity * 1.3))
    elif town == 'varna':
        print('{0:.2f}'.format(quantity * 1.35))
elif product == 'peanuts':
    if town == 'sofia':
        print('{0:.2f}'.format(quantity * 1.6))
    elif town == 'plovdiv':
        print('{0:.2f}'.format(quantity * 1.5))
    elif town == 'varna':
        print('{0:.2f}'.format(quantity * 1.55))