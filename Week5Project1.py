#This program accepts input from three sides of a triangle
#and determines if sides are equilateral

#Get input for 3 sides of triangle
side1 = int(input("Enter a number for side 1: "))
side2 = int(input("Enter a number for side 2: "))
side3 = int(input("Enter a number for side 3: "))

triangle = [side1, side2, side3]

if side1 == side2 and side2 == side3:
    print("This is an equilateral triangle with sides of", triangle, "inches")

else:
    print("Sorry, this is not an equilateral triangle.\
The sides are", triangle, "inches")

    

