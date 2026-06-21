import numpy as np

eqn1 = input("Enter first equation: ")
eqn2 = input("Enter second equation: ")

def f(x,y):
    try:
        return eval(eqn1)
    except (SyntaxError, ZeroDivisionError, NameError, TypeError):
        print("Invalid input.")
        exit(0)


def g(x,y):
    try:
        return eval(eqn2)
    except (SyntaxError, ZeroDivisionError, NameError, TypeError):
        print("Invalid input.")
        exit(0)


def fx(x, y, h=1e-6):
    return (f(x+h, y) - f(x, y))/h

def fy(x, y, h=1e-6):
    return (f(x, y+h) - f(x, y))/h

def gx(x, y, h=1e-6):
    return (g(x+h, y) - g(x, y))/h

def gy(x, y, h=1e-6):
    return (g(x, y+h) - g(x, y))/h

x0,y0 = map(float, input("Enter initial guesses separated by space: ").split())

N = int(input("Enter no. of iterations: "))
E = float(input("Enter tolerable error: "))
count = 1


while count <= N:
    F = f(x0,y0)
    G = g(x0,y0)
    Fx = fx(x0,y0)
    Fy = fy(x0,y0)
    Gx = gx(x0,y0)
    Gy = gy(x0,y0)
    #matrix elements
    # a11 = fx(x0,y0)
    # a12 = fy(x0,y0)
    # a21 = gx(x0,y0)
    # a22 = gy(x0,y0)

    D = Fx*Gy - Fy*Gx

    if abs(D) < 1e-12:
        print("Jacobian matrix is singular. Choose another initial guesses.")
        break
    else:
        Dx = F*Gy - G*Fy
        Dy = G*Fx - F*Gx

        x1 = x0 - (Dx/D)
        y1 = y0 - (Dy/D)

    err_x = abs(x1-x0)
    err_y = abs(y1-y0)

    if err_x < E and err_y < E:
        print(f"Root is {x1:.2f} and {y1:.2f} reached in {count} iterations.")
        break
    else:
        x0 = x1
        y0 = y1
        count += 1


    if count > N:
        print(f"No solution is converged in {N} solutions.")



    





    









