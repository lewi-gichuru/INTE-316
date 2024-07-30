import numpy as np

def lagrange_basis_polynomials(x_points, x):
    """ Compute the Lagrange basis polynomials at x for given x_points """
    n = len(x_points)
    L = np.ones(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                L[i] *= (x - x_points[j]) / (x_points[i] - x_points[j])
    return L

def lagrange_interpolation(x_points, y_points):
    """ Compute the Lagrange polynomial coefficients for given data points """
    n = len(x_points)
    coefficients = np.zeros(n)
    
    for i in range(n):
        basis_poly = lagrange_basis_polynomials(x_points, x_points[i])
        coefficients += y_points[i] * basis_poly
    
    return coefficients

# Given data points
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]

# Compute Lagrange polynomial coefficients
coefficients = lagrange_interpolation(x_points, y_points)
print("Lagrange Polynomial Coefficients:", coefficients)

# Optionally, create a polynomial function using the computed coefficients
def lagrange_polynomial(x):
    L = 0
    for i in range(len(coefficients)):
        L += coefficients[i] * np.prod([(x - x_points[j]) / (x_points[i] - x_points[j]) for j in range(len(x_points)) if j != i])
    return L

# Example usage
print("L(2.5) =", lagrange_polynomial(2.5))  # Example evaluation of the Lagrange polynomial at x = 2.5
