
base = int(input('Enter a new destination base (2-9): '))
max_number = base ** 4 - 1
print('4-digit maximum number in the new destination base is %d' % max_number)
decimal_number = float(input('Enter a decimal number: '))
x = decimal_number / base

remainder = (float(x) - int(x)) * base
d1 = '%d' % remainder

x_2 = int(x) / base
remainder_2 = (float(x_2) - int(x_2)) * base
d2 = '%d' % remainder_2

x_3 = int(x_2) / base
remainder_3 = (float(x_3) - int(x_3)) * base
d3 = '%d' % remainder_3

x_4 = int(x_3) / base
remainder_4 = (float(x_4) - int(x_4)) * base
d4 = '%d' % remainder_4

result = d4+d3+d2+d1
print('The new number with the new base is ' + result)


























