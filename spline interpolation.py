import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Generate example data
np.random.seed(0)  # For reproducibility
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Create a cubic spline interpolation
cs = CubicSpline(x, y)

# Generate points for plotting the spline
x_fit = np.linspace(0, 10, 1000)
y_fit = cs(x_fit)

# Plot the original data points
plt.scatter(x, y, color='blue', label='Data')

# Plot the cubic spline interpolation
plt.plot(x_fit, y_fit, color='red', label='Cubic Spline')

# Adding labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Spline Interpolation')
plt.legend()
plt.show()
