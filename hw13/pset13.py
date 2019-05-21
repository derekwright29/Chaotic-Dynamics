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

class aRK4(object):

    def __init__(self, *functions):

        """
        Initialize a RK4 solver.
        :param functions: The functions to solve.
        """

        self.f = functions
        self.t = 0


    def solve(self, y, h, n, TOL):

        """
        Solve the system ODEs.
        :param y: A list of starting values. An initial condition
        :param h: Step size.
        :param n: Endpoint.
        :param TOL: L-infinity tolerance to change h-step
        """

        t = []
        res = []
        for i in y:
            res.append([])

        while self.t <= n and h != 0:
            t.append(self.t)
            #take full h step
            y = self._solve(y, self.t, h) # y is next point

            # Adaptive adjustments
            y2 = self._solve(y, self.t, h/2) # y2 is first half-step point
            y2 = self._solve(y2, self.t+h/2, h/2)  # y2 is overwritten to be the second half-step; update self.t+h/2 accordingly, as well as giveing the start point fo the old y2
            err = max([abs(y[i]-y2[i]) for i in range(0, len(y))])  #take L-infinity norm
            # if we are within bounds
            if err < TOL:
                for c, i in enumerate(y):
                    res[c].append(i)
                self.t += h
                if err < TOL/2:
                    h = h*2
            else:
                for c, i in enumerate(y2):
                    res[c].append(i)
                self.t += h
                h = h/2


            if self.t + h > n:
                h = n - self.t

        self._reset()
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

    def _reset(self):
        self.t = 0

import numpy as np
import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

ADAPTIVE = 0

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax = plt.axes(projection='3d')
#ax.set_top_view()
#ax.view_init(270,270)

G = 1
m1 = 0.5
m2 = 0.5
m3 = 0.5

distcube = lambda r1x,r1y,r1z,r2x,r2y,r2z: ((r1x - r2x)**2 + (r1y-r2y)**2 + (r1z-r2z)**2)**(3/2)

r1xdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: v1x
r1ydot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: v1y
r1zdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: v1z
v1xdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: -G*m2*(r1x-r2x) / distcube(r1x,r1y,r1z,r2x,r2y,r2z) - G*m3*(r1x-r3x) / distcube(r1x,r1y,r1z,r3x,r3y,r3z)
v1ydot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: -G*m2*(r1y-r2y) / distcube(r1x,r1y,r1z,r2x,r2y,r2z) - G*m3*(r1y-r3y) / distcube(r1x,r1y,r1z,r3x,r3y,r3z)
v1zdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: -G*m2*(r1z-r2z) / distcube(r1x,r1y,r1z,r2x,r2y,r2z) - G*m3*(r1z-r3z) / distcube(r1x,r1y,r1z,r3x,r3y,r3z)
r2xdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: v2x
r2ydot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: v2y
r2zdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: v2z
v2xdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: -G*m1*(r2x-r1x) / distcube(r1x,r1y,r1z,r2x,r2y,r2z) - G*m3*(r2x-r3x) / distcube(r2x,r2y,r2z,r3x,r3y,r3z)
v2ydot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: -G*m1*(r2y-r1y) / distcube(r1x,r1y,r1z,r2x,r2y,r2z) - G*m3*(r2y-r3y) / distcube(r2x,r2y,r2z,r3x,r3y,r3z)
v2zdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: -G*m1*(r2z-r1z) / distcube(r1x,r1y,r1z,r2x,r2y,r2z) - G*m3*(r2z-r3z) / distcube(r2x,r2y,r2z,r3x,r3y,r3z)
r3xdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: v3x
r3ydot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: v3y
r3zdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: v3z
v3xdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: -G*m1*(r3x-r1x) / distcube(r1x,r1y,r1z,r3x,r3y,r3z) - G*m2*(r3x-r2x) / distcube(r2x,r2y,r2z,r3x,r3y,r3z)
v3ydot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: -G*m1*(r3y-r1y) / distcube(r1x,r1y,r1z,r3x,r3y,r3z) - G*m2*(r3y-r2y) / distcube(r2x,r2y,r2z,r3x,r3y,r3z)
v3zdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z, r3x, r3y, r3z, v3x, v3y, v3z: -G*m1*(r3z-r1z) / distcube(r1x,r1y,r1z,r3x,r3y,r3z) - G*m2*(r3z-r2z) / distcube(r2x,r2y,r2z,r3x,r3y,r3z)

duration = 701
plotstep = 500 #100
prev_init = 0
prev = prev_init
init = [[0,0,0,0,0,0,1,0,0,0,1,0,0,40,0,0,-.15,0],[0,0,0,0,0,0,1,0,0,0,1,0,0,23,0,0,-.15,0]] #[0,0,0,0,0,0,1,0,0,0,1,0,0.5,5000,0,0,0,0],
threebody = RK4(r1xdot, r1ydot, r1zdot, v1xdot, v1ydot, v1zdot, r2xdot, r2ydot, r2zdot, v2xdot, v2ydot, v2zdot, r3xdot, r3ydot, r3zdot, v3xdot, v3ydot, v3zdot)
#threebody = aRK4(r1xdot, r1ydot, r1zdot, v1xdot, v1ydot, v1zdot, r2xdot, r2ydot, r2zdot, v2xdot, v2ydot, v2zdot, r3xdot, r3ydot, r3zdot, v3xdot, v3ydot, v3zdot)
#i= init[1]
for i in init:
    strt = time.time()
    t, y = threebody.solve(i, 0.005, duration)

    threebody.reset()
    print "Done solving"
    print time.time() - strt


    # R1X,R1Y,R1Z = zip(y[0],y[1],y[2])
    # R2X,R2Y,R2Z = zip(y[6],y[7],y[8])

    # ax.scatter3D(y[0], y[1], y[2], s=1, lw=0, color='red')
    # ax.scatter(y[0], y[1], s=1, lw=0)
    # ax.scatter(y[6], y[7], s=1, lw=0)
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    #ax.set_zlabel('Z')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title("Planar ThreeBody System")
    plt.xlabel('X')
    plt.ylabel('Y')
    prev = prev_init
    for j in range(prev,len(t), plotstep):
        ax.scatter(y[0][prev:j], y[1][prev:j], s=1, lw=0, color='blue')
        ax.scatter(y[6][prev:j], y[7][prev:j], s=1, lw=0,color='orange')
        ax.scatter(y[12][prev:j], y[13][prev:j], s=1, lw=0,color='lightgreen')
        plt.pause(.00001)
        prev = j
    print "Done plotting"
    plt.cla()
    plt.clf()


    plt.title("Planar ThreeBody System " + str(i[12:15]) +str(plotstep)+ '_' + str(duration))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.scatter(y[0][prev_init:],y[1][prev_init:], s=1,lw=0)
    plt.scatter(y[6][prev_init:],y[7][prev_init:], s=1,lw=0)
    plt.scatter(y[12][prev_init],y[13][prev_init], s=1,lw=0)
    plt.savefig("images/ThreeBodySyst" + str(i[12:15]) +str(plotstep)+str(duration) + ".png", dpi=500)
    plt.close()
    dt = time.time() - strt
    print dt
