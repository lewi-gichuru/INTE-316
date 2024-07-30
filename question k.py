import numpy as np

# Define the function
def f(x, y):
    return x**2 + y**2 + x*y + x - y + 1

# Define the partial derivatives
def dfdx(x, y):
    return 2*x + y + 1

def dfdy(x, y):
    return 2*y + x - 1

# Gradient Descent function
def gradient_descent(learning_rate=0.1, num_iterations=1000, tolerance=1e-6):
    x, y = 0, 0  # Initial guess
    for _ in range(num_iterations):
        grad_x = dfdx(x, y)
        grad_y = dfdy(x, y)
        
        # Update x and y
        x_new = x - learning_rate * grad_x
        y_new = y - learning_rate * grad_y
        
        # Check for convergence
        if np.sqrt((x_new - x)**2 + (y_new - y)**2) < tolerance:
            break
        
        x, y = x_new, y_new
        
    return x, y

# Run Gradient Descent
x_min, y_min = gradient_descent()
print(f"Minimum point: x = {x_min}, y = {y_min}")
print(f"Minimum value: f(x, y) = {f(x_min, y_min)}")
