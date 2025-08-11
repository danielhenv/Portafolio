def area_square(side):
    return side * side

def area_circle(radius):
    import math
    return math.pi * radius ** 2

side = float(input("Side of the square: "))
radius = float(input("Radius of the circle: "))

print(f"Area of the square: {area_square(side)}")
print(f"Area of the circle: {area_circle(radius):.2f}")