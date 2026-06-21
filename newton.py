# import numpy as np
# import matplotlib.pyplot as plt


# eqn = input("enter your non-linear equation: ")

# def f(x):
#     try:
#         return eval(eqn)
#     except (SyntaxError, TypeError, ValueError, NameError):
#         print("Invalid equation!!!")
#         exit(0)

# def g(f,x,h=1e-6):
#     return (f(x+h)-f(x-h))/(2*h)

# x0 = float(input("enter initial guess: "))

# if abs(g(f,x0))< 1e-6:
#     print("Root can't be find.")
#     exit(0)

# else:
#     N = int(input("enter max no. of iterations: "))
#     E = float(input("enter tolerable error: "))
#     M = []
#     count = 1

#     while count<=N:
#         x1 = x0 - (f(x0)/g(f,x0))
#         M.append(x1)

#         error = abs(x1-x0)

#         if error < E:
#             break
#         else:
#             x0 = x1
#         count+=1
        
#     if count > N:
#         print(f"solution doesn't reach in {N} iterations.")
#     else:
#         print(f"root is {x1} obtained in {count} iterations.")
#         M = np.array(M)
#         x = np.linspace(x0-1,x0+1,1000)
#         y = np.zeros_like(M)

#         fig,ax = plt.subplots(figsize=(8,4))
#         ax.plot(x,f(x),label='f(x)', color='blue')
#         ax.scatter(M,y,marker='x')

#         for j,z in enumerate(M):
#             plt.text(z,0,str(j+1))
        
#         ax.scatter(M,f(M))
#         ax.axhline(0,color='green')
#         ax.axvline(0,color='green')
#         ax.set_xlabel("x-axis")
#         ax.set_ylabel("y-axis")
#         ax.set_title("Lab")
#         ax.grid()
#         plt.show()

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# eqn = input("Enter the equation in x using Python syntax: ")

# def F(x, eqn):
#     return eval(eqn)

# def f(x):
#     return F(x, eqn)

# def g(f, x, h=1e-10):
#     return (f(x+h) - f(x-h)) / (2*h)

# a = float(input(f"Enter your initial approximation: "))

# if g(f, a) == 0:
#     print("The derivative is zero. Choose another approximation.")
# else:
#     e = float(input(f"Enter the tolerable error: "))
#     N = int(input("Enter the max number of iterations: "))
#     itr = 1
#     list = []
#     while itr <= N:   
#         b = a - (f(a) / g(f, a))
#         if (g(f, b) == 0):
#             print("The slope tends to zero. Hence the function does not converge.")
#             break
#         error = abs((b - a) / b)
#         # list.append([itr, a, f(a), g(f, a), b])
#         if error <= e:
#             print(f"The root is {b} in iteration {itr} with error {error}")
#             # list = pd.DataFrame(list, columns=['Iterations', 'Xn', 'f(Xn)', "f'(Xn)", 'Xn+1'])
#             # for _, row in list.iterrows():
#             #     print(' '.join(str(x) for x in row))
#             #     print()
#             #     print()
#             break
#         a = b
#         itr += 1
#     if (itr > N):
#         print(f"Solution does not converge in {itr} iterations")
#     x = np.linspace(-5, 5, 1000)
#     plt.plot(x, [f(i) for i in x], color='blue', label='f(x)')
#     # plt.plot(x, [g(f, i) for i in x], color='red', label="f'(x)")
#     plt.axhline(0, color='black')
#     plt.axvline(0, color='black')
#     plt.legend()
#     plt.grid(True)
#     plt.title('Newton-Raphson Method Visualization')
#     plt.show()



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
    x1 = x0  # safe default in case loop never runs

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
        # plt.show()