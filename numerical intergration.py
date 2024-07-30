import numpy as np

def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    return integral

# Example function
def f(x):
    return np.sin(x)

# Integrate sin(x) from 0 to pi
a, b = 0, np.pi
n = 1000
result_trap = trapezoidal_rule(f, a, b, n)
print(f"Trapezoidal Rule: {result_trap}")

#simpsons rule
def simpsons_rule(f, a, b, n):
    if n % 2:
        n += 1  # n must be even
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[n])
    return integral

# Integrate sin(x) from 0 to pi
result_simp = simpsons_rule(f, a, b, n)
print(f"Simpson's Rule: {result_simp}")

#gaussian quadrature
from scipy.integrate import quad

# Integrate sin(x) from 0 to pi
result_gauss, _ = quad(f, a, b)
print(f"Gaussian Quadrature: {result_gauss}")

#monte carlo intergration 
def monte_carlo_integration(f, a, b, num_samples=10000):
    x = np.random.uniform(a, b, num_samples)
    y = f(x)
    integral = (b - a) * np.mean(y)
    return integral

# Integrate sin(x) from 0 to pi
result_monte_carlo = monte_carlo_integration(f, a, b)
print(f"Monte Carlo Integration: {result_monte_carlo}")
