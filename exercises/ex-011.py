# PAINTING WALL

# Make a program that reads the wall's height and width in meters,
# calcs its area and paint quantity needed to paint it,
# knowing that each paint litre paints an area of 2 squared meters

height = float(input('height: '))
width = float(input('width: '))

area = height * width
paint = area / 2
print('You need {:.1f}L to paint an area of {:.1f}m²'.format(paint, area))
