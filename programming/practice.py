import math

def compute_area_square (side):
    return side*side

def compute_area_rectangle (lenght, width):
    return lenght*width

def compute_area_circle (radius):
    return radius**2 * math.pi

shape = ""

while shape != "quit":

    shape = input("For what shape would you like to find an area? ")
    shape = shape.lower()
    
    if shape == "square":
        side= float(input("What is the length of a side of the square?"))
        area= compute_area_square (side)
        print(f"The area of the square is: {area:.2f}")

    elif shape == "rectangle":
        lenght= float(input("What is the length of rectangle?"))
        width=float(input("What is the width of the rectangle?"))
        area= compute_area_rectangle (lenght, width)
        print(f"The area of the rectangle is: {area:.2f}")

    elif shape == "circle":
        radius= float(input("What is the radius of the circle?"))
        area = compute_area_circle (radius)
        print(f"The area of the circle is: {area:.2f}")
        
    elif shape != "quit":
        print("That is not a shape")
        