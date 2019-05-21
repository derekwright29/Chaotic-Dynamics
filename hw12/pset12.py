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

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax = plt.axes(projection='3d')
#ax.set_top_view()
#ax.view_init(270,270)

G = 1
m1 = 0.5
m2 = 0.5

distcube = lambda r1x,r1y,r1z,r2x,r2y,r2z: ((r1x - r2x)**2 + (r1y-r2y)**2 + (r1z-r2z)**2)**(3/2)

r1xdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: v1x
r1ydot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: v1y
r1zdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: v1z
v1xdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: -G*m2*(r1x-r2x) / distcube(r1x,r1y,r1z,r2x,r2y,r2z)
v1ydot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: -G*m2*(r1y-r2y) / distcube(r1x,r1y,r1z,r2x,r2y,r2z)
v1zdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: -G*m2*(r1z-r2z) / distcube(r1x,r1y,r1z,r2x,r2y,r2z)
r2xdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: v2x
r2ydot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: v2y
r2zdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: v2z
v2xdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: -G*m1*(r2x-r1x) / distcube(r1x,r1y,r1z,r2x,r2y,r2z)
v2ydot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: -G*m1*(r2y-r1y) / distcube(r1x,r1y,r1z,r2x,r2y,r2z)
v2zdot = lambda t, r1x, r1y, r1z, v1x, v1y, v1z, r2x, r2y, r2z, v2x, v2y, v2z: -G*m1*(r2z-r1z) / distcube(r1x,r1y,r1z,r2x,r2y,r2z)

init = [[0,0,0,0,0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,1,0,1,0,0]]
mode = 'Y'
binary = RK4(r1xdot, r1ydot, r1zdot, v1xdot, v1ydot, v1zdot, r2xdot, r2ydot, r2zdot, v2xdot, v2ydot, v2zdot)

for i in init:
    strt = time.time()
    t, y = binary.solve(i, 0.0005, 40)
    print len(t)
    binary.reset()
    print "Done solving"


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
    plt.title("Planar Binary System")
    plt.xlabel('X')
    plt.ylabel('Y')
    prev = 0
    for i in range(0,len(t), 500):
        ax.scatter(y[0][prev:i], y[1][prev:i], s=1, lw=0, color='blue')
        ax.scatter(y[6][prev:i], y[7][prev:i], s=1, lw=0,color='orange')
        plt.pause(.00001)
        prev = i
    print "Done plotting"
    plt.cla()
    plt.clf()


    # if mode is 'Y':
    #     plt.ylim(-.5, 20.5)
    # else:
    #     plt.xlim(-.5,20.5)
    plt.scatter(y[0],y[1], s=1,lw=0)
    plt.scatter(y[6],y[7], s=1,lw=0)
    plt.savefig("images/BinarySystem_" + mode + ".png", dpi=500)
    plt.close()
    mode = 'X'
    dt = time.time() - strt
    print dt
