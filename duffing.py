#!/usr/bin/env python3 
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import numba as nb


def y_dot(t,y,x,nu,F):
    return -(nu*y)+x-(x**3)+(F*np.cos(t))

def x_dot(y):
    return y

@nb.jit 
def rk(a, b, x0, y0, nu=0, F=0, xdot = x_dot, ydot = y_dot):
    dt = 0.001
    start = 2*a*np.pi
    end = 2*b*np.pi
    n = int(np.ceil((end-start)/dt))
    t = np.linspace(start,end,n)
    # Create empty vectors to be filled
    x_vec = np.zeros(n)
    y_vec = np.zeros(n)
    x_dot_vec = np.zeros(n)
    y_dot_vec = np.zeros(n)
    # Fill initial points
    x_vec[0] = x0
    y_vec[0] = y0
    for k in range(n):
        # Fill dot vectors
        x_dot_vec[k] = x_dot(y_vec[k])
        y_dot_vec[k] = ydot(t[k],y_vec[k],x_vec[k],nu,F)
        # Fill position vectors
        if k == n-1:
            break
        else:
            K1y = dt*ydot(t[k],y_vec[k],x_vec[k],nu,F)
            K2y = dt*ydot((t[k]+dt/2),(y_vec[k]+K1y/2),x_vec[k],nu,F)
            K3y = dt*ydot((t[k]+dt/2),(y_vec[k]+K2y/2),x_vec[k],nu,F)
            K4y = dt*ydot((t[k]+dt),(y_vec[k]+K3y),x_vec[k],nu,F)
            RKy = (K1y+(2*K2y)+(2*K3y)+K4y)/6
            y_vec[k+1] = y_vec[k]+RKy

            K1x = dt*xdot(y_vec[k])
            K2x = dt*xdot(y_vec[k]+K1x/2)
            K3x = dt*xdot(y_vec[k]+K2x/2)
            K4x = dt*xdot(y_vec[k]+K3x)
            RKx = (K1x+(2*K2x)+(2*K3x)+K4x)/6
            x_vec[k+1] = x_vec[k]+RKx
    return (t,x_vec,y_vec)

def plot(x,t,title=''):
    plt.rc('text', usetex=True)
    plt.plot(x,t,color="green")
    plt.xlabel(r'$x$', fontsize = 19)
    plt.ylabel(r'$t$', fontsize = 19)
    plt.xticks(fontsize = 17)
    plt.yticks(fontsize = 17)
    plt.title(title, fontsize = 21)
    plt.show()


def parametric_plot(x,y,title = ''):
    plt.rc('text', usetex=True)
    plt.plot(x,y,color="green")
    plt.xlabel(r'$x$', fontsize = 19)
    plt.ylabel(r'$\dot{x}$', fontsize = 19)
    plt.xticks(fontsize = 17)
    plt.yticks(fontsize = 17)
    plt.title(title, fontsize = 21)
    plt.show()

def scatter_plot(x,y,n,title = ''):
    plt.rc('text', usetex=True)
    ax = plt.subplot
    )
    plt.xlabel(r'$x$', fontsize = 19)
    plt.ylabel(r'$\dot{x}$', fontsize = 19)
    plt.xticks(fontsize = 17)
    plt.yticks(fontsize = 17)
    plt.title(title, fontsize = 21
    for k in range(n):
        plt.scatter(x[6283*k],y[6283*k],color='g')
    plt.show()

    
## define a recursive function for chnaging parameters      
def gif(t,)