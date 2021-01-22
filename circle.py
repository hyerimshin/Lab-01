PI = 3.14159
radius = float(input('Enter a radius value: '))
double_radius = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius
double_circumference = 2 * PI * double_radius
double_area = PI * double_radius * double_radius
circumference_division = double_circumference / circumference
area_division = double_area / area

print('circumference: %.2f' % circumference)
print('area: %.2f' % area)
print('circumference of circle with double radius: %.2f' % double_circumference)
print('area of circle with double radius: %.2f' % double_area)
print('when you double radius, the value of circumference increase %d times' % circumference_division)
print('when you double radius, the value of area increase %d times' % area_division)


