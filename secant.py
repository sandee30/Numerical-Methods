import numpy as np
import matplotlib.pyplot as plt

eqn = input("Enter your equation: ")

def f(x):
    try:
        return eval(eqn)
    except (SyntaxError, ValueError, TypeError,
            ZeroDivisionError, NameError):
        print("Invalid equation!")
        exit(0)

a, b = map(float, input("Enter two initial guesses: ").split())

N = int(input("Enter maximum iterations: "))
E = float(input("Enter error tolerance: "))

M = []

count = 1

while count <= N:

    if (f(b) - f(a)) == 0:
        print("Division by zero encountered.")
        exit(0)

# Root = 0.5053077493926499

    # c = b - (f(b) * (b - a)) / (f(b) - f(a))
    c = (a*f(b)-b*f(a))/(f(b)-f(a))
    error = abs(c - b)

    M.append(c)

    if error < E:
        break

    a = b
    b = c
    count += 1

if count > N:
    print("Solution does not converge.")
else:
    print(f"\nRoot = {c}")
    print(f"Obtained in {count} iterations\n")

    

    M = np.array(M)
    x = np.linspace(a-1,a+1,1000)
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