def circle_calc(radius):
    area = 3.14 * radius**2
    circumference = 2 * 3.14 * radius
    diameter = 2 * radius
    return area , circumference , diameter

def main():
    Radius = int(input("Enter the radius of the circle: "))
    area, circumference, diameter = circle_calc(Radius)
    print(f"{round(area,2)} {round(circumference,2)} {round(diameter,2)}")
if __name__ == '__main__':
    main()