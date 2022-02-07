# converting pounds and kilogram each other

weight = input('weight: ')
unit = input('lbs or kg: ')
a = 0.45 * int(weight)
b = 2.205 * int(weight)
if unit == 'l' or unit == 'L':
    print(f'weight of the person: {a}'+' kg')
elif unit == 'k' or unit == 'K':
    print(f'weight of person is :{b}'+' lbs')

