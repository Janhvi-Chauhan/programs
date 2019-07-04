from math import *
options = {
    "Circle": 1,
    "Square": 2,
    "Rectangle": 3
}
print(options)
choice = int(input("Enter your choice : "))
if choice == 1:
    r = int(input("Enter radius of circle : "))
    area = pi*r*r
    print("Area = ", area)
elif choice == 2:
    side = int(input("Enter side of the square : "))
    area = side*side
    print("Area = ", area)
elif choice == 3:
    length = int(input("Enter length of rectangle : "))
    breadth = int(input("Enter breadth of the rectangle : "))
    area = length * breadth
    print("Area = ", area)
