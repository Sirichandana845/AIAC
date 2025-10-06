def rectangle_area(length, width):
    return length * width

def square_area(side, _=0):
    return side * side

def circle_area(radius, _=0):
    return 3.14 * radius * radius

AREA_FUNCTIONS = {
    "rectangle": rectangle_area,
    "square": square_area,
    "circle": circle_area
}

def calculate_area(shape, x, y=0):
    func = AREA_FUNCTIONS.get(shape)
    if func:
        return func(x, y)
    raise ValueError(f"Unknown shape: {shape}")
# example_usage:
print(calculate_area("rectangle", 5, 10))  # Output: 50
print(calculate_area("square", 4))          # Output: 16
print(calculate_area("circle", 3))          # Output: 28.26