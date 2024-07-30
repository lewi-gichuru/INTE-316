import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the model function
def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

# Generate example data
np.random.seed(0)  # For reproducibility
x_data = np.linspace(-5, 5, 25)
y_data =2.8 * x_data**2 + 2 * x_data + 1 + np.random.normal(0, 5, size=x_data.size)

# Fit the model to the data
initial_guess = [1, 1, 1]  # Initial guess for the parameters a, b, c
params, covariance = curve_fit(quadratic_model, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
a, b, c = params
print(f"Fitted parameters: a = {a}, b = {b}, c = {c}")

# Generate the fitted curve
y_fit = quadratic_model(x_data, a, b, c)

# Plot the data and the fitted curve
plt.scatter(x_data, y_data, label='Data', color='blue', s=10)
plt.plot(x_data, y_fit, label='Fitted curve', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Curve Fitting Example')
plt.show()
