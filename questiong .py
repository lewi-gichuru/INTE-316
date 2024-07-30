def trapezoidal_rule(f, a, b, n):
    """
    Approximate the integral of f from a to b using the trapezoidal rule with n subintervals.
    
    Parameters:
    f : function
        The function to integrate.
    a : float
        The start point of the interval.
    b : float
        The end point of the interval.
    n : int
        The number of subintervals.
    
    Returns:
    float
        The approximate value of the integral.
    """
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        integral += f(a + i * h)
    
    integral *= h
    return integral

# Example usage:
def f(x):
    return x**2  # Define the function to integrate

a = 0  # Lower limit of integration
b = 1  # Upper limit of integration
n = 10  # Number of subintervals

result = trapezoidal_rule(f, a, b, n)
print(f"Approximate integral of f(x) from {a} to {b} is {result:.6f}")
