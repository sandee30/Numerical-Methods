import numpy as np
#input number of equations
n = int(input("Enter the number of equations: "))
#input augmented matrix
A = []
for i in range(n):
	row = list(map(float, input(f"Enter coefficients and constant term for equation {i+1}, separated by spaces: ").split()))
	if len(row) != n + 1:
		raise ValueError("Each row must have n coefficients and 1 constant term.")
	A.append(row)
 
A = np.matrix(A)
print("\nThe augmented matrix is:")
print(A)

# Gauss Elimination
for i in range(n):
    if A[i, i] == 0:
        raise ValueError("Mathematical Error: Pivot Element is Zero.")
    for j in range(i+1, n):
        ratio = A[j, i]/A[i, i]
        for k in range(n+1):
            A[j, k] = A[j, k] - ratio * A[i, k]
x = np.zeros(n)
# Displaying the upper triangular matrix
print("\nThe upper triangular matrix is:")
print(A)
# Back Substitution
x[n-1] = A[n-1,n]/A[n-1,n-1]
for i in range(n-2,-1,-1):
    x[i] = A[i,n]
    for j in range(i+1,n):
        x[i] = x[i] - A[i,j]*x[j]
    x[i] = x[i]/A[i,i]
# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
