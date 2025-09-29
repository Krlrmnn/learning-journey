side1 = int(input("Enter length of side 1: "))
side2 = int(input("Enter length of side 2: "))
side3 = int(input("Enter length of side 3: "))

if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Error: Side lengths must be positive.")
elif (side1 + side2 > side3 and 
      side1 + side3 > side2 and 
      side2 + side3 > side1):
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("Error: Not a valid triangle.")