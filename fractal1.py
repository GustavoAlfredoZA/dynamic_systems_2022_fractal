#!/usr/bin/env python3
import numpy as np
import math
import matplotlib.pyplot as plt

def square(x,y,b,l,s):
    Q1 = [(x-(l/2.0)),y]
    Q2 = [(x+(l/2.0)),y]
    Q3 = [(x+(l/2.0)),(y+l)]
    Q4 = [(x-(l/2.0)),(y+l)]
    return [Q1[0],Q2[0],Q3[0],Q4[0],Q1[0] ] , [Q1[1],Q2[1],Q3[1],Q4[1],Q1[1]]

def computeCoordinates(x, y, l, b, x_Q1, y_Q1, x_Q2, y_Q2, x_Q3, y_Q3, x_Q4, y_Q4):
    l1 = l / 3.0
    b1 = 0
    b2 = 3
    b3 = 2
    b4 = 1
    x_r1= x
    y_r1= y+l
    x_r2= x+(l*2/3)
    y_r2= y+(l/3)
    x_r3= x
    y_r3= y-l/3
    x_r4= x-(l*2/3)
    y_r4= y+(l/3)
    return l1, b1,b2,b3,b4, x_r1, y_r1, x_r2, y_r2, x_r3, y_r3 , x_r4, y_r4

def fractal(n, ax, x, y, b, l):
    if n > 0:
        X, Y = square(x,y,b,l,1)
        ax.plot(X,Y, 'b', linewidth=0.5)
        if l!=1:
            ax.plot(X[b:b+2],Y[b:b+2], color= '#b6cff2', linewidth=1)

        l1,b1,b2,b3,b4,x_r1,y_r1,x_r2,y_r2,x_r3,y_r3,x_r4,y_r4=computeCoordinates(x,y,l,b,X[0], Y[0], X[1], Y[1], X[2], Y[2], X[3], Y[3])
        fractal(n-1,ax, x_r1, y_r1,b1,l1)
        fractal(n-1,ax, x_r2, y_r2,b2,l1)
        fractal(n-1,ax, x_r3, y_r3,b3,l1)
        fractal(n-1,ax, x_r4, y_r4,b4,l1)

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    #P0
    x=0.0
    y=0.0
    b=0
    l=1.0
    fractal(5, ax, x, y, b, l)
    plt.savefig('fractal.png')
    plt.show()



if __name__ == '__main__':
    main()
