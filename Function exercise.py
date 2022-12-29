# Write a function called calculate_area that takes base and height
# as an input and returns and area of a triangle. Equation of an
# area of a triangle is,
# area = (1/2)*base*height
# Modify above function to take third parameter shape type.
# It can be either "triangle" or "rectangle". Based on shape
# type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape


def calculate_area(base, height, shape="triangle"):
    if shape == "rectangle":
        return base * height
    return 0.5 * base * height


print(f"Are is : {calculate_area(5, 10.5, 'triangle')}")

# Write a function called print_pattern that takes
# integer number as an argument and prints following
# pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
#
# *
# **
# ***
# ****


def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(0, i):
            print("*", end='')
        print()


number = int(input())
print_pattern(number)
