"""
author: Nashita Halim
date: 19/2/26
Making Variables
"""
import math

#input
radius = int(input("Input radius of a circle: "))
length_rect = int(input("Input length of rectangle: "))
width_rect = int(input("Input width of rectangle: "))
side_length_octagon = int(input("Input side length of octagon: "))


#processing

#CIRCLE
a_circle = (math.pi)*(radius**2)
p_circle = 2*(math.pi)*radius


#rect
a_rect = (length_rect)*(width_rect)
p_rect = 2*(length_rect+width_rect)

#octagon

a_oct = 2*(1+2**0.5)*side_length_octagon**2
p_oct = 8*side_length_octagon

#output

print (f"The circle has an area of {a_circle} and a perimeter of {p_circle}")
print (f"The rectangle has an area of {a_rect} and a perimeter of {p_rect}")
print (f"The octogan has an area of {a_oct} and a perimeter of {p_oct}")