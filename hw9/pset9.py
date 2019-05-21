from __future__ import division
import matplotlib
import math
from scipy import spatial
import numpy as np

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

# Chaotic Trajectory
# a = 16
# r = 45
# b = 4

# Non-chaotic trajectory
a = 16
r = 45
b = 4

xdot = lambda t, x, y, z: (a*(y-x))
ydot = lambda t, x, y, z: ((r*x)-y-(x*z))
zdot = lambda t, x, y, z: ((x*y)-(b*z))

init = [-13,-12,52]

lorenz = RK4(xdot, ydot, zdot)
t, vect = lorenz.solve(init, 1*10**-3, 15)

fourple = [vect[0], vect[1], vect[2], t]
spacio_points = list(zip(*vect))
temporalspacio_points = list(zip(*fourple))

Ndt = float(t[-1]-t[0])

def Wolf(fidoosh, epsilon, theiler, Ndeltat):
    '''
    fidoosh is fiduciary trajectory (fourples)
    epsilon is the distance threshold
    theiler is an integer, denoting how many time steps to exclude from findNNeighbor
    Ndeltat is the duration of the trajectory. Normalization factor at the end
    '''
    end_time = fidoosh[3][-1]
    #init return lists
    Ls = []
    Lprimes = []
    dts = []

    m = 100
    while(m < len(fidoosh)):
        print("M: ", m)
        x_t = fidoosh[m]
        if m != 0:
            z_t = findNNeighbor(x_t, theiler)
        else:
            z_t = findNNeighbor(x_t, theiler)        #account for first case

        Lp, mstep = distanceStepping(x_t, z_t, epsilon)
        if mstep is not 100:
            Ls.append(distance(x_t, z_t))
            Lprimes.append(Lp)
        #print ("Ls: ", Ls)
        #print("Lprimes: ", Lprimes)
        m += mstep

    big_lyap = 1/Ndeltat * sum([math.log((np.array(Lprimes, dtype=np.float)/np.array(Ls, dtype=np.float))[i]) for i in range(len(Lprimes))])
    return big_lyap

def findNNeighbor(x, theiler):
    '''
    x is single point
    theiler is the keep out region (traj[x +/- theiler] will be excluded)

    returns distance to nearest Neighbor
    returns timestamp index of found neighbor
    '''
    try:
        assert(len(set(temporalspacio_points)) == len(temporalspacio_points))
    except:
        print("trajectory not unique: THERE'S A DUPE")
        assert(0)
    point_index = temporalspacio_points.index(x)
    theiler_window = spacio_points[point_index-theiler:point_index+theiler+1]
    NN_tree = spatial.KDTree(spacio_points)
    i=1
    try:
        while (i < theiler*2+1):
            if (spacio_points[NN_tree.query(x[:3],k=theiler*10)[1][i]] not in theiler_window): #we have to concatenate x so that it matches the shape of NN_tree
                return temporalspacio_points[NN_tree.query(x[:3],k=theiler*10)[1][i]]
            else:
                i += 1
    except ValueError:
        print("bitch, your theiler window is probably too small")

def distance(x, z):
    '''
    x, z are n-dimensional points

    returns distance
    '''
    print("In distance")

    squares = 0
    for i in range(0,len(x)-1):
        squares += (x[i]-float(z[i]))**2
    return(math.sqrt(squares))

def distanceStepping(x, z, epsilon):
    '''
    x is fidoosh fourple
    z is neighbor fourple
    epsilon is distance threshold
    '''
    print("in Distance Stepping")
    print("X: ", x)
    print("Z: ", z)

    z_time_index = int(z[3] / (t[1]-t[0]))       #take time of point, divide by timestep gives time index
    print("Z_t_index: ", z_time_index)
    x_time_index = int(x[3] / (t[1]-t[0]))
    print("X_t_index: ", x_time_index)

    dist = distance(x,z)
    if dist > epsilon:
        print ("Dist too big: ", dist)
        return dist, 100

    i = 0
    while (dist < epsilon and ((x_time_index + i) < len(t)-1) and (z_time_index + i) < len(t)-1):
        try:
            dist = distance(spacio_points[x_time_index + i], spacio_points[z_time_index + i])
        except:
            return dist, i
        print("Dist: ", dist)
        print("I: ", i)
        i += 1
    return dist, i

print(Wolf(temporalspacio_points, 1, 100, Ndt))

#numpy.linalg.eig



# -2.1863111152816486
#
