print("LU FACTORISATION METHOD OF SOLVING SYSTEM OF LINEAR EQUATIONS")

import numpy as np
np.set_printoptions(suppress=True, precision=4)


n = int(input("Enter no. of variables: "))
A = []

for i in range(n):
    row = list(map(float, input(f"Enter coefficients for equation {i+1} (including RHS): ").split()))
    if len(row) != n + 1:
        raise ValueError(f"Each row must have {n+1} values (coefficients + RHS).")
    A.append(row)

A = np.array(A)
b = A[:, n]          # Extract RHS column
A = A[:, :n]         # Extract coefficient matrix

print(f"\nCoefficient matrix [A]:\n{A}")
print(f"RHS vector [b]: {b}")

# --- LU Decomposition ---
L = np.zeros((n, n))
U = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i == 0:
            U[i][j] = A[i][j]
        if i == j:
            L[i][j] = 1
        if i != j and i < j:
            L[i][j] = 0
        if i != j and i > j:
            U[i][j] = 0
        if j == 0 and i >= 1:
            L[i][j] = A[i][j] / U[j][j]

        s = 0
        for k in range(j):
            if i >= 1 and j >= 1 and i <= j:
                s += L[i][k] * U[k][j]
        if i >= 1 and j >= 1 and i <= j:
            U[i][j] = A[i][j] - s

        s = 0
        for t in range(j):
            if i >= 1 and j >= 1 and i > j:
                s += L[i][t] * U[t][j]
        if i >= 1 and j >= 1 and i > j:
            L[i][j] = (A[i][j] - s) / U[j][j]

print(f"\nLower triangular matrix [L]:\n{L}")
print(f"Upper triangular matrix [U]:\n{U}")



v = np.zeros(n)
for i in range(n):
    s = sum(L[i][j] * v[j] for j in range(i))
    v[i] = (b[i] - s) / L[i][i]

print(f"\nIntermediate vector [v] (from Lv = b): {v}")


x = np.zeros(n)
for i in range(n - 1, -1, -1):
    s = sum(U[i][j] * x[j] for j in range(i + 1, n))
    x[i] = (v[i] - s) / U[i][i]

print(f"\nSolution vector [x]:")
for i in range(n):
    print(f"  x{i+1} = {x[i]:.2f}")

