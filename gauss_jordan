import numpy as np
np.set_printoptions(suppress=True, precision=4)

n = int(input("Enter the number of equations: "))
A = []
for i in range(n):
    row = list(map(float, input(f"Enter coefficients and constant for equation {i+1}: ").split()))
    if len(row) != n + 1:
        raise ValueError("Each row must have n coefficients and 1 constant term.")
    A.append(row)

A = np.array(A, dtype=float)        
print("\nAugmented matrix:\n", A)

for i in range(n):
    max_row = i + np.argmax(np.abs(A[i:, i]))
    A[[i, max_row]] = A[[max_row, i]]

    pivot = A[i, i]
    if pivot == 0:
        raise ValueError("Matrix is singular — no unique solution.")
    A[i] = A[i] / pivot

    for j in range(n):
        if j != i:
            A[j] = A[j] - A[i] * A[j, i]

print("\nReduced Row Echelon Form (RREF):\n", A)

print("\nSolution:")
for i in range(n):
    print(f"  x{i+1} = {round(A[i, -1], 4)}")   
