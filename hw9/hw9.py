from __future__ import division
import matplotlib
import math
from scipy import spatial
import pdb

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

lorentz = RK4(xdot, ydot, zdot)
t, vect = lorentz.solve(init, 1*10**-3, 1)

fourple = [vect[0], vect[1], vect[2], t]
spacio_points = zip(*vect)
temporalspacio_points = zip(*fourple)
print len(spacio_points)

Ndt = float(t[-1]-t[0])

def Wolf(fidoosh, times, epsilon, theiler, Ndeltat):
    '''
    fidoosh is fiduciary trajectory
    times is timestamp list
    epsilon is the distacne threshold
    theiler is an integer, denoting how many time steps to exclude from findNNeighbor
    '''
    end_time = times[-1]
    #init return lists
    Ls = []
    Lprimes = []
    dts = []

    m = 0
    while(m < len(times)):
        x_t = fidoosh[m]
        if m != 0:
            z_t = findNNeighbor(x_t[:-1], theiler)
        else:
            z_t = findNNeighbor(x_t[:-1], theiler)        #account for first case
        Ls.append(distance(x_t, z_t))
        Lp, mstep = distanceStepping(x_t, z_t, epsilon)
        Lprimes.append(Lp)
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
        assert(len(set(spacio_points)) == len(spacio_points))
    except:
        print("trajectory not unique: THERE'S A DUPE")
        assert(0)
    point_index = spacio_points.index(x)
    theiler_window = spacio_points[point_index-theiler:point_index+theiler+1]
    NN_tree = spatial.KDTree(spacio_points)
    for i in range(theiler*2+1):
        if (spacio_points[int(NN_tree.query(x)[1])] not in theiler_window):
            return temporalspacio_points[NN_tree.query(x)[1]]
        else:
            i += 1
    return -1

def distance(x,y):
#     '''
#     x is a n-dimensional points
#     y is also an n-dimensional point
#
#     return distance
#     '''
    squares = 0
    for i in range(0,len(x)-1):
        squares += (x[i]-y[i])**2
    return math.sqrt(squares)


def distanceStepping(x, z, epsilon):
    '''
    x is fidoosh fourple
    z is neighbor fourple
    epsilon is distance threshold
    '''
    #pdb.set_trace()
    z_time_index = int(z[3] / (t[1]-t[0]))       #take time of point, divide by timestep gives time index
    x_time_index = int(x[3] / (t[1]-t[0]))

    dist = distance(x,z)
    i = 0
    while (dist < epsilon and i < len(x)):
        try:
            dist = distance(temporalspacio_points[x_time_index + i], temporalspacio_points[z_time_index + i])
        except IndexError as err:
            print "X_ind: " , x_time_index
            print "Z_ind: ", z_time_index
            print "i: ", i
            print "hit the end, Keegan"
            pass
        i += 1
    return dist, i


print(Wolf(temporalspacio_points, t, 5, 2, Ndt))
