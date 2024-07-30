import numpy as np
import matplotlib.pyplot as plt

# Define data points
x = np.arange(1, 7)  # x values from 1 to 6
y = [5.5, 43.1, 128, 290.7, 498.4, 978.67]  # Given y values

# Fit a 4th-degree polynomial
p = np.polyfit(x, y, 4)

# Generate new x values for plotting the polynomial
x2 = np.arange(1, 7)

# Evaluate the polynomial at the new x values
y2 = np.polyval(p, x2)

# Plot the data points and the fitted polynomial
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x2, y2, label='Fitted Curve')
plt.grid(True)
plt.legend()
plt.show()
