"""
Plot a Harmonograph
"""

import numpy as np
import matplotlib.pyplot as plt

def harmonograph(a,b,c,d,e,f,n):
    t = np.linspace(0, 2*np.pi, n)
    x = np.sin(a*t + d) + c*np.cos(b*t + e)
    y = np.sin(a*t + f) + c*np.cos(b*t)
    return x,y

def main():
    a = 1
    b = -3
    c = -7
    d = 50
    e = 9
    f = 405
    n = 1000
    x,y = harmonograph(a,b,c,d,e,f,n)
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    main()