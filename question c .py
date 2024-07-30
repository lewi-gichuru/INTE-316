def linear_interpolation(x1, y1, x2, y2, x):
    return y1 + (y2 - y1) / (x2 - x1) * (x - x1)

# Given points
x1, y1 = 2.00, 7.2
x2, y2 = 4.25, 7.1

# Point to interpolate
x = 4.0

# Calculate y
y = linear_interpolation(x1, y1, x2, y2, x)
print(f"The value of y at x = {x} is {y}")
