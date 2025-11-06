import numpy as np, matplotlib.pyplot as plt
# Семейство графиков
def grf1(x):
    return np.sin(0.8*x)**2+np.exp(np.cos(x))
def grf2(x):
    return np.exp(np.cos(2*x))-3*np.sin(0.5*x)+0.4

xn=0
xk=np.pi*6
nn=200
X=np.linspace(xn,xk,nn)
Y,Z=grf1(X),grf2(X)
plt.plot(X,Y)
plt.plot(X,Z)
plt.show()