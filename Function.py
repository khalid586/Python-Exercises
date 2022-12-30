import math


def circle_calc(radius):
    Area = math.pi * radius**2
    Circumference = 2 * math.pi * radius
    Diameter = 2 * radius
    return Area, Circumference, Diameter


if __name__ == '__main__':
    Radius = float(input("Enter the radius of the circle: "))
    area, circumference, diameter = circle_calc(Radius)
    print(f"Area = {round(area, 2)}, Circumference =  {round(circumference, 2)} , Diameter = {round(diameter, 2)}")
