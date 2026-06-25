import numpy as np
import matplotlib.pyplot as plt


eqn = input("enter your non-linear equation: ")

def f(x):
    try:
        return eval(eqn)
    except (SyntaxError, TypeError, ValueError, NameError):
        print("Invalid equation!!!")
        exit(0)

def g(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

x0 = float(input("enter initial guess: "))

if abs(g(f, x0)) == 0:
    print("Root can't be found: derivative is zero at the initial guess.")
    exit(0)

else:
    N = int(input("enter max no. of iterations: "))
    E = float(input("enter tolerable error: "))
    M = []
    count = 1
    x1 = x0 

    while count <= N:
        deriv = g(f, x0)

        if abs(deriv) < 1e-12:
            print(f"Derivative became too small at iteration {count}. Stopping.")
            break

        x1 = x0 - (f(x0) / deriv)
        M.append(x1)

        error = abs(x1 - x0)

        if error < E:
            break

        x0 = x1
        count += 1

    if count > N:
        print(f"solution doesn't reach in {N} iterations.")
    else:
        print(f"root is {x1} obtained in {count} iterations.")

        M = np.array(M)
        x = np.linspace(x1 - 1, x1 + 1, 1000)
        y = np.zeros_like(M)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x, f(x), label='f(x)', color='blue')
        ax.scatter(M, y, marker='x')

        for j, z in enumerate(M):
            plt.text(z, 0, str(j + 1))

        ax.scatter(M, f(M))
        ax.axhline(0, color='green')
        ax.axvline(0, color='green')
        ax.set_xlabel("x-axis")
        ax.set_ylabel("y-axis")
        ax.set_title("Lab")
        ax.grid()
        ax.legend()
        plt.show()
