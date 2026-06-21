# False - position method

import numpy as np
import matplotlib.pyplot as plt

eqn = input("Enter a non-linear equation: ")

def f(x):
    try:
        return eval(eqn)
    except (SyntaxError, ValueError, TypeError, NameError):
        print("Invalid equation!")
        exit(0)

x1,x2 = map(float, input("Enter two initial guesses: ").split())


if f(x1) * f(x2) >= 0:
    print(f"No root lies in the interval [{x1}, {x2}]")
    exit(0)

e = float(input("Enter tolerable error: "))
N = int(input("Enter maximum number of iterations: "))

a = x1
b = x2

itr = 1
M = []

while itr <= N:

    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    M.append(c)

    if abs(f(c)) < e:
        print(f"\nApproximate root = {c}")
        print(f"Iterations = {itr}")
        break

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

    itr += 1

if itr > N:
    print(f"\nSolution not found within {N} iterations.")
else:
    M = np.array(M)
    x = np.linspace(x1-1,x2+1,1000)
    y = np.zeros_like(M)
    fig,ax = plt.subplots(figsize=(8,4))
    ax.plot(x,f(x),label='f(x)', color='blue')
    ax.scatter(M,y,marker='x')

    for j,z in enumerate(M):
      plt.text(z,0,str(j+1))
    
    ax.scatter(M,f(M))
    ax.axhline(0,color='green')
    ax.axvline(0,color='green')
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_title("Lab")
    ax.grid()
    plt.show()