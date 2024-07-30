import numpy as np

def divided_differences(x, y):
    """ Compute the divided difference table for given data points. """
    n = len(x)
    # Initialize the divided difference table
    F = np.zeros((n, n))
    F[:,0] = y
    
    # Compute divided differences
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i+1][j-1] - F[i][j-1]) / (x[i+j] - x[i])
    
    return F

def newton_polynomial_coefficients(x, F):
    """ Compute the coefficients of the Newton polynomial from the divided difference table. """
    n = len(x)
    coefficients = [F[0][i] for i in range(n)]
    return coefficients

def newton_interpolation(x, y):
    """ Compute Newton interpolating polynomial coefficients for given data points. """
    F = divided_differences(x, y)
    coefficients = newton_polynomial_coefficients(x, F)
    return coefficients

def newton_polynomial(x, coefficients, x_points):
    """ Evaluate the Newton polynomial at given x using the computed coefficients. """
    n = len(coefficients)
    result = coefficients[0]
    for i in range(1, n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - x_points[j])
        result += term
    return result

# Given data points
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]

# Compute Newton polynomial coefficients
coefficients = newton_interpolation(x_points, y_points)
print("Newton Polynomial Coefficients:", coefficients)

# Example usage: Evaluate the Newton polynomial at x = 2.5
x_val = 2.5
y_val = newton_polynomial(x_val, coefficients, x_points)
print("P(2.5) =", y_val)
