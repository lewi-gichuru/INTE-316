import numpy as np

def power_iteration(A, num_iterations=1000, tolerance=1e-6):
    n, m = A.shape
    b_k = np.random.rand(n)
    
    for _ in range(num_iterations):
        # Calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)
        
        # Calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        
        # Re normalize the vector
        b_k = b_k1 / b_k1_norm
        
        # Check for convergence
        if np.linalg.norm(np.dot(A, b_k) - b_k1_norm * b_k) < tolerance:
            break
            
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k))
    eigenvector = b_k
    
    return eigenvalue, eigenvector

def qr_algorithm(A, num_iterations=1000, tolerance=1e-6):
    n, m = A.shape
    A_k = A.copy()
    Q_total = np.eye(n)
    
    for _ in range(num_iterations):
        Q, R = np.linalg.qr(A_k)
        A_k = np.dot(R, Q)
        Q_total = np.dot(Q_total, Q)
        
        # Check for convergence
        off_diagonal_norm = np.sqrt(np.sum(np.tril(A_k, -1)**2 + np.triu(A_k, 1)**2))
        if off_diagonal_norm < tolerance:
            break
            
    eigenvalues = np.diag(A_k)
    eigenvectors = Q_total
    
    return eigenvalues, eigenvectors

# Example matrix
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

eigenvalue_power, eigenvector_power = power_iteration(A)
print("Power Iteration Method:")
print(f"Eigenvalue: {eigenvalue_power}")
print(f"Eigenvector: {eigenvector_power}")

eigenvalues_qr, eigenvectors_qr = qr_algorithm(A)
print("\nQR Algorithm:")
print(f"Eigenvalues: {eigenvalues_qr}")
print(f"Eigenvectors: \n{eigenvectors_qr}")

# Comparing the results
print("\nComparison:")

print("\nPower Iteration Method:")
print(f"Dominant Eigenvalue: {eigenvalue_power}")
print(f"Corresponding Eigenvector: {eigenvector_power}")

print("\nQR Algorithm:")
print(f"Eigenvalues: {eigenvalues_qr}")
print(f"Eigenvectors: \n{eigenvectors_qr}")

# Differences
print("\nDifferences:")
print("The Power Iteration method provides only the dominant eigenvalue and its corresponding eigenvector.")
print("The QR Algorithm provides all the eigenvalues and their corresponding eigenvectors.")
