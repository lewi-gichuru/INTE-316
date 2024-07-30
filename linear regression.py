import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate example data
np.random.seed(0)  # For reproducibility
x = 2 * np.random.rand(100, 1)  # 100 data points between 0 and 2
y = 4 + 3 * x + np.random.randn(100, 1)  # Linear relation with noise

# Plot the data
plt.scatter(x, y, color='blue', label='Data')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Generated Data')
plt.legend()
plt.show()

# Create and fit the linear regression model
model = LinearRegression()
model.fit(x, y)

# Print the parameters of the fitted line
print(f"Intercept: {model.intercept_[0]}")
print(f"Slope: {model.coef_[0][0]}")

# Predict y values using the fitted model
x_fit = np.linspace(0, 2, 100).reshape(-1, 1)  # 100 points for plotting
y_fit = model.predict(x_fit)

# Plot the data and the fitted line
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x_fit, y_fit, color='red', label='Fitted line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.legend()
plt.show()
