from __future__ import division
import matplotlib
import math
from scipy import spatial
import numpy as np
import pylab as pl

class RK4(object):

    def __init__(self, *functions):

        """
        Initialize a RK4 solver.
        :param functions: The functions to solve.
        """

        self.f = functions
        self.t = 0


    def solve(self, y, h, n):

        """
        Solve the system ODEs.
        :param y: A list of starting values.
        :param h: Step size.
        :param n: Endpoint.
        """

        t = []
        res = []
        for i in y:
            res.append([])

        while self.t <= n and h != 0:
            t.append(self.t)
            y = self._solve(y, self.t, h)
            for c, i in enumerate(y):
                res[c].append(i)

            self.t += h

            if self.t + h > n:
                h = n - self.t

        return t, res


    def _solve(self, y, t, h):

        functions = self.f

        k1 = []
        for f in functions:
            k1.append(h * f(t, *y))

        k2 = []
        for f in functions:
            k2.append(h * f(t + .5*h, *[y[i] + .5*h*k1[i] for i in range(0, len(y))]))

        k3 = []
        for f in functions:
            k3.append(h * f(t + .5*h, *[y[i] + .5*h*k2[i] for i in range(0, len(y))]))

        k4 = []
        for f in functions:
            k4.append(h * f(t + h, *[y[i] + h*k3[i] for i in range(0, len(y))]))

        return [y[i] + (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) / 6.0 for i in range(0, len(y))]

    def reset(self):
        self.t = 0

a = 16
r = 45
b = 4

xdot = lambda t, x, y, z: (a*(y-x))
ydot = lambda t, x, y, z: ((r*x)-y-(x*z))
zdot = lambda t, x, y, z: ((x*y)-(b*z))

init = [-13,-12,52]

lorenz = RK4(xdot, ydot, zdot)
dur = 30
t, vect = lorenz.solve(init, 1*10**-3, dur)

def boxcounting(points):
    # specifying a variety of box sizes
    # NOTE: tinkering with the lower bound can result in really nasty crashes, so FOR THE SAKE OF ALL THAT IS HOLY, DON'T GO LOWER THAN -3
    leng = -4
    num_pts = 100
    sizes=np.logspace(leng, 6, num=num_pts, endpoint=False, base=2)
    
    # compute the minimum and maximum of each dimension, aka bounding box on the data
    Xmax = max(points[0])
    Xmin = min(points[0])
    Ymax = max(points[1])
    Ymin = min(points[1])
    Zmax = max(points[2])
    Zmin = min(points[2])
    
    Nepsilon=[]
    
    # looping over all of the box sizes we specified earlier
    for size in sizes:
        print("Size : ",size)
        
        # computing the multi-dimensional histogram where the bounds of the histogram are determined by the bounding box of the data
        H, edges=np.histogramdd(points, bins=(np.arange(Xmin,Xmax,size),np.arange(Ymin,Ymax,size),np.arange(Zmin,Zmax,size)))
        
        # compute the number of non-empty histogram bins and then add that number to our list
        print np.sum(H>0)
        Nepsilon.append(np.sum(H>0))
         
    # fit a line to our points 
    # coeffs=np.polyfit(np.log(sizes), np.log(Nepsilon), 1)
    print len(sizes)
    print len(Nepsilon)
    # log-log plot of the number of the size of the boxes vs the number of boxes
    pl.plot(np.log(1/sizes),np.log(Nepsilon), '.')
    # pl.plot(np.log(1/sizes), np.polyval(coeffs,np.log(sizes)))
    pl.title('Box Counting Dimension: Lorentz ' + str(leng))
    pl.xlabel('log $1/\epsilon$')
    pl.ylabel('log $N(\epsilon)$')
    pl.savefig('Box_counting_lorentz_long_'+str(dur) + '_' + str(leng)+'.png')
     
    # return(coeffs[0], pl)
    return(pl)

boxcounting(vect).show()

###### DEBUGGER ZONE #####