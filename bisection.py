import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter your eqn: ")

def f(x):
  try:
    return eval(eqn)
  except (SyntaxError, ZeroDivisionError, ValueError, TypeError):
    print("Invalid input!!!")
    exit(0)

a,b = map(float, input("Enter two initial guesses: ").split())
M = []
T = []

if f(a)*f(b)>=0:
  print("root not found.")
  exit(0)
else:
  print("root lies inside")
  N = int(input("enter no. of iterations: "))
  E = float(input("Enter error tolerance: "))
  count = 1

  while count <= N:
    c = (a+b)/2
    T.append([count,a,b,c,f(a),f(b),f(c),abs(a-b)])
    M.append(c)
    if f(c)==0:
      break
    elif f(a)*f(c)<0:
      b = c
    else:
      a = c
    error = abs(a-b)
    if error < E:
      break
    else:
      count+=1
    
  if count > N:
    print("The solution doesn't converge.")
  else:
    print(f"The solution is {c} reached in {count} iterations.")
    table = pd.DataFrame(T,columns=['iterations','a','b','c','fa','fb','fc','error'])
    print(table.to_string(index=False))
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