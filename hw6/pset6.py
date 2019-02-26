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

import pylab
import math

A = .92
beta = 0.25
m = .1
g = 9.8
l = .1
alpha = .75 * math.sqrt(g/l)

thetaDotDot = lambda t, theta, thetaDot: (A*math.cos(alpha*t)-(m*g*math.sin(theta))-(beta*l*thetaDot))/(m*l)
thetaDot = lambda t, theta, thetaDot: thetaDot

pend = RK4(thetaDot, thetaDotDot)

poinEvals = [[],[]]
bigT = (2*math.pi/alpha)
runlength = 850

t, theta = pend.solve([.01,0], 1*10**-3, runlength)
print len(t)

# f = [s % bigT for s in t]

# # # Old shit boi
# for n in range(int(math.floor((runlength+1)/bigT))):
#     for i in range(len(t)):
#         if ((t[i-1] < n*bigT) and (n*bigT < t[i])):
#             poinEvals[0].append(theta[0][i-1])
#             poinEvals[1].append(theta[1][i-1])


# Old shit boi
for n in range(int(math.floor((runlength+1)/bigT))):
    for i in range(len(t)):
        if ((t[i-1] < n*bigT) and (n*bigT < t[i])):
            poinEvals[0].append((theta[0][i-1]+theta[0][i])/2)      # linear interpolation
            poinEvals[1].append((theta[1][i-1]+theta[1][i])/2)

print "Poins:", len(poinEvals[0])
print poinEvals[0]
print poinEvals[1]

# # New unshit boi
# for i in range(len(f)):
#     if ((f[i-1] < bigT) and (bigT< f[i])):
#         poinEvals[0].append(theta[0][i-1])
#         poinEvals[1].append(theta[1][i-1])

# pend.reset()


pylab.scatter(poinEvals[0], poinEvals[1], s=5, lw=0)
pylab.xlabel('theta')
pylab.ylabel('omega')
pylab.title('Chaotic Poincare Section w/ Lin Interpolation')
pylab.savefig("test2a_001_linint.png", dpi=300)
pylab.show()



# poinEvals = [[],[]]


# len(poinEvals[0])
# 
# pylab.grid()
# pylab.scatter(theta[0], theta[1], s=1)
# pylab.xlabel('theta')
# pylab.ylabel('omega')
# pylab.title('dt=.00001')
# pylab.show()
# 
# poinEvals