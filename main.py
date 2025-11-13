# -----------------------------
# 1. Full Production Output
# -----------------------------
import numpy as np

# Industry
x11 = 840
x12 = 500
# Industrial product demand
y1 = 950
# Total output x1
x1 = x11 + x12 + y1

# Agriculture
x21 = 460
x22 = 450
# Agricultural product demand
y2 = 680
# Total output x2
x2 = x21 + x22 + y2

# Forecasted demand for next year
c1 = 1060
c2 = 750

# Technological matrix A (a[i,j] = x[i,j] / x[j])
A = np.array([[x11/x1, x12/x1],
              [x21/x2, x22/x2]])
print("A =", A)

# Compute new total outputs x to meet forecasted demand
c = np.array([[c1], [c2]])
print("c =", c)
E = np.array([[1, 0], [0, 1]])
B = np.linalg.inv(np.subtract(E, A))
print("B =", B)
x = np.dot(B, c)
print("x =", x)


# -----------------------------
# 2. Frobenius Number & Price Vector Analysis
# -----------------------------
import numpy as np

# Input data
A = np.array([
    [0.3, 0.3, 0.2],
    [0.2, 0.15, 0.1],
    [0.15, 0.4, 0.25]
])
s = np.array([0.25, 0.45, 0.3])

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)

# Characteristic polynomial
polynomial = np.poly(A)
print("Characteristic polynomial coefficients:", polynomial)

# Frobenius number (largest eigenvalue)
frobnumber = max(eigenvalues)
print("Frobenius number:", frobnumber)

# Right Frobenius vector
print("Right Frobenius vector:", eigenvectors[:, 0])

# Left Frobenius vector (eigenvector of A^T)
AT = np.transpose(A)
eigenvaluesT, eigenvectorsT = np.linalg.eig(AT)
print("Left Frobenius vector:", eigenvectorsT[:, 0])

# Check productivity
if frobnumber < 1:
    print("Matrix is productive: the economic system can operate stably.")
else:
    print("Matrix is not productive: the system is unstable.")

# Full cost matrix B = (E - A)^(-1)
try:
    B = np.linalg.inv(np.subtract(np.identity(3), A))
    print("Full cost matrix B:")
    print(B)
except np.linalg.LinAlgError:
    print("Matrix (E - A) is singular, cannot compute full cost matrix.")
    B = None

# Series convergence check E + A + A^2 + ... + A^N
accuracy = 0.01
K = np.zeros((3, 3))
prev_K = np.zeros((3, 3))
N = 0

while True:
    prev_K = K.copy()
    K = np.add(K, np.linalg.matrix_power(A, N))
    N += 1
    if np.all(np.abs(K - prev_K) < accuracy):
        print("Series converges at step N =", N)
        print("Series sum:")
        print(K)
        break

# Price vector P = B^T * s
if B is not None:
    P = np.dot(np.transpose(B), s)
    print("Price vector P:", P)
    if np.all(P > 0):
        print("All prices are positive (economically valid).")
    else:
        print("Warning: Price vector contains zero or negative values!")
