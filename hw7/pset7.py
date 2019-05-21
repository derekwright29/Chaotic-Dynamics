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
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Lorentz Attractor ICs and lambdas

a = 16
r = 13.3
b = 4

xdot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz: (a*(y-x))
ydot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz: ((r*x)-y-(x*z))
zdot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz: ((x*y)-(b*z))
dxxdot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz: -a*dxx + a*dxy
dxydot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz: (r-z)*dxx - dxy - x*dxz
dxzdot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz: y*dxx+x*dxy-b*dxz
dyxdot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz: -a*dyx + a*dyy
dyydot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz:(r-z)*dyx - dyy - x*dyz
dyzdot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz: y*dyx+x*dyy-b*dyz
dzxdot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz: -a*dzx + a*dzy
dzydot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz:(r-z)*dzx - dzy - x*dzz
dzzdot = lambda t, x, y, z, dxx, dxy, dxz, dyx, dyy, dyz, dzx, dzy, dzz: y*dzx+x*dzy-b*dzz

init = [[10,-5,2,1,0,0,0,1,0,0,0,1]
        ]

lorenz = RK4(xdot, ydot, zdot, dxxdot, dxydot, dxzdot, dyxdot, dyydot, dyzdot, dzxdot, dzydot, dzzdot)

for i in init:
    t, results = lorenz.solve(i, 1*10**-3, 10)
    lorenz.reset()
    print("IC:" + str(i))
    v1 = []
    v2 = []
    v3 = []
    v4 = []
    for j in range(len(results)):
        if 0<=j<=2:
            v1.append(results[j][len(results[j]) - 1])
        elif 3<=j<=5:
            v2.append(results[j][len(results[j]) - 1])
        elif 6<=j<=8:
            v3.append(results[j][len(results[j]) - 1])
        else:
            v4.append(results[j][len(results[j]) - 1])
    mat = np.matrix([v2,v3,v4])
    real_mat = mat.transpose()

    print(real_mat)
    eigs = np.linalg.eig(real_mat)
    print(eigs)
    print("printing lyaps")
    for k in eigs[0]:
        print(math.log(abs(k))/10)

    print("column sums:" + str(mat.sum(axis=0)))
    origin = [0,0,0]
    X, Y, Z = zip(origin,origin,origin)
    U, V, W = zip(v2,v3,v4)
    #C = [(250,10,10),(30,230,30),(10,120,210)]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(X,Y,Z,U,V,W,arrow_length_ratio=.1)
    X,Y,Z = zip(origin,origin,origin)
    U, V, W = zip([1,0,0],[0,1,0],[0,0,1])
    ax.quiver(X,Y,Z,U,V,W,arrow_length_ratio=.3, color='red')
    ax.set_xlim(-0.5, 3)
    ax.set_ylim(-1,6)
    ax.set_zlim(-1,4)
    eleva = 30
    azimu = 30
    ax.view_init(eleva, azimu)
    plt.savefig("pset7Figure4" + str(i[:3]) + ".png", dpi=300)
    eleva = 30
    azimu = -30
    ax.view_init(eleva, azimu)
    plt.savefig("pset7Figure5" + str(i[:3]) + ".png", dpi=300)
    eleva = 30
    azimu = 60
    ax.view_init(eleva, azimu)
    plt.savefig("pset7Figure6" + str(i[:3]) + ".png", dpi=300)


plt.show()


# /* with 10^-3
# IC:[0, 1, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1]
# [[ 2.361  5.087  0.46 ]
#  [ 1.886  4.135  0.358]
#  [-0.028 -0.086  0.665]]
# column sums:[[4.219 9.136 1.483]]
# IC:[10, -5, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1]
# [[ 2.12   3.884  3.028]
#  [ 1.631  3.023  2.462]
#  [-0.478 -1.101  0.01 ]]
# column sums:[[3.273 5.806 5.5  ]]
# IC:[0, -1, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1]
# [[ 2.361  5.087 -0.46 ]
#  [ 1.886  4.135 -0.358]
#  [ 0.028  0.086  0.665]]
# column sums:[[ 4.275  9.308 -0.153]]
# */



#with 10^-5
# /*
#
# IC:[0, 1, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1]
# [[ 2.404  5.174  0.481]
#  [ 1.919  4.206  0.374]
#  [-0.03  -0.089  0.665]]
# IC:[10, -5, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1]
# [[ 2.131  3.86   3.121]
#  [ 1.639  3.008  2.532]
#  [-0.486 -1.11  -0.018]]
# IC:[0, -1, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1]
# [[ 2.404  5.174 -0.481]
#  [ 1.919  4.206 -0.374]
#  [ 0.03   0.089  0.665]]*/
