from aRK4 import aRK4
from rungaKutta4 import RK4
import matplotlib.pyplot as plt

import mpl_toolkits.mplot3d

TOLs = [0.1]
start_step = 0.01
duration = 5
#
a = 16
r = 45
b = 4


######## Loretnz System
Xdot = lambda t, X, Y, Z: a*(Y - X)
Ydot = lambda t, X, Y, Z: r*X - Y - X*Z
Zdot = lambda t, X, Y, Z: X*Y - b*Z
LorSys = aRK4(Xdot, Ydot, Zdot)

# ######### Rossler System
# a = .398
# b = 2
# c = 4
#
# Xdot = lambda t, X, Y, Z: -(Y + Z)
# Ydot = lambda t, X, Y, Z: X + a*Y
# Zdot = lambda t, X, Y, Z: b + Z*(X - c)
#
# RosSys = aRK4(Xdot, Ydot, Zdot)

# Old RK for comparison
pend = RK4(Xdot, Ydot, Zdot)

ics = [[-13,-12,52]]

for i in ics:
    for tol in TOLs:
        t, y = LorSys.solve(i, start_step, duration, tol)
        t = [abs(t[j] - t[j+1]) for j in range(0, len(t)-1)]
        t_o, y_o = pend.solve(i, start_step, duration)
        t_o = [abs(t_o[j] - t_o[j + 1]) for j in range(0, len(t_o)-1)]
        print len(y[0]), len(y_o[0])
        print 't_mean: ' + str(sum(t)/len(t))
        print 't_old_mean: ' + str(sum(t_o) / len(t_o))
        fig = plt.figure()
        plt.grid()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(y[0], y[1], y[2], zdir='z', s=1, lw=0, c='#33337F')
        ax.scatter(y_o[0], y_o[1], y_o[2], zdir='z', s=1, lw=0, c='#7F3333')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        eleva = 0
        azimu = -90
        ax.view_init(elev=eleva, azim=azimu)
        ax.set_title("Lorentz System: Duration " + str(duration) + '_Tol' + str(tol))
        plt.savefig('test4Lorentz_v2' + str(duration) + '_' + str(tol) + '.png', dpi=500)
        plt.show()
        plt.close()


plt.close()



