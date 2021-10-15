#This program accepts input from three sides of a triangle
#and determines if this is a right triangle

from math import sqrt

print("Side 3 will be designated as the hypotenuse.")

side1 = int(input("Enter a number for side 1: "))
side2 = int(input("Enter a number for side 2: "))
side3 = (int(input("Enter a number for side 3: "))**2)

#Calculate the hypotenuse
hypotenuse = ((side1 ** 2 ) + (side2 ** 2 ))


if side3 == hypotenuse:
    print("This is a right triangle!!!")
    print("The hypotenuse equals", hypotenuse)
    
else:
    print("Sorry, this is not a Right Triangle.")





