import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2 + 2*x + 1

# Create an array of x values
x = np.linspace(-8, 8, 64)
y = f(x)

# Calculate the numerical derivative
dy_dx = np.gradient(y, x)

# Plot the function and its derivative
plt.figure(figsize=(5, 5))
plt.plot(x, y, label='f(x)')
plt.plot(x, dy_dx, label="f'(x)", linestyle='--')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function and its Derivative (Numerical)')
plt.grid(True)
plt.show()