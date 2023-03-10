# Write a Python program to read the three sides of a triangle and print whether the triangle is equilateral, isosceles or scalene.

# For taking 3 sides of trianagle
side1 = float(input('Enter the 1st side of trianglr ::'))
side2 = float(input('Enter the 2nd side of trianglr ::'))
side3 = float(input('Enter the 3rd side of trianglr ::'))

if (side1==side2==side3):
    print('Triangle is equilateral')
elif((side1 !=side2)and(side2!=side3)and(side3!=side1)):
    print('Triangle is scalene')
else:
    print('Triangle is isoscles')






