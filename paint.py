COVERAGE = 40
length = float(input('what is the length of the room in meter?: '))
width = float(input('what is the width of the room in meter?: '))
height = float(input('what is the height of the room in meter?: '))
coats = int(input('how many coats will paint in the room?: '))
surface_area = 2 * (width * height + height * length) + width * length
coverage_needed = surface_area * coats
cans_of_paint_required = coverage_needed / COVERAGE

if float(cans_of_paint_required) > int(cans_of_paint_required):
    print('you need to buy %d Cans' % (int(cans_of_paint_required) + 1 ))








