from rungaKutta4 import RK4
import pylab
import math

A = 0                #   .8
beta = 0        #.25
m = .1
g = 9.8
l = .1
alpha = 0 #0.75 * (math.sqrt(g/l))

Tdotdot = lambda t, T, Tdot: (A*math.cos(alpha*t)-(m*g*math.sin(T))-(beta*l*Tdot))/(m*l)
Tdot = lambda t, T, Tdot: Tdot

pend = RK4(Tdot, Tdotdot)


t,y = pend.solve([0.01, 0], 10**-5, .6365)
# pylab.grid()
# pylab.scatter(y[0], y[1], lw=0, s=1,c='#7F7F7F')
# pylab.xlabel('Theta')
# pylab.ylabel('omega')
# pylab.show()

####### TODO: Make MUCH more modular. Pass in I.C.s, shift, modulo, plot them###########
# init_conds = [ [2,0],
#                [0,40],
#                [5,-40],
#
#
#
#
# ]
#

# ######### PROBLEM 6 ########
# for i in [.92]:
#     A = i
#     t, y = pend.solve([2, 0], .0001, 60)
#     y[0] = [(y[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y[0]))]     # mod 2pi
#     pylab.grid()
#     pylab.scatter(y[0][300000:], y[1][300000:], c='#7F7F7F', lw=0, s=1)
#     pylab.title('Long A Value:' + str(A))
#     pylab.xlabel('Theta')
#     pylab.ylabel('omega')
#     pylab.savefig(r'hw4_p6/A_Value_L_sT:' + str(A) + '.png')
#     pylab.close()
    #
    # .5?
    # .4 double cycle?
    # .7 back to periodic
    # .8 really interesting
    # .87?
    # .89?
    # .92? ### BINGOOO
    # .97?

########    PROBLEM 4   ##############
# t, y = pend.solve([.01, 0], .01, 5.8)
# t2, y2 = pend.solve([0, 40], 1*10**-4, 2)
# t3, y3 = pend.solve([5, -32], 1*10**-4, 2)
# # t5, y5 = pend.solve([-math.pi+.01, 0], 1*10**-3, 2)
# t6, y6 = pend.solve([9.2, -1.5], 1*10**-4, 2)
# t7, y7 = pend.solve([3, 10], 1*10**-4, 2)
# t8, y8 = pend.solve([math.pi+.01, 1.5], 1*10**-4, 2)
# t10, y10 = pend.solve([-math.pi-.01, 7], 1*10**-4, 2)
# t11, y11 = pend.solve([-9, 21], 1*10**-4, 2)
# t12, y12 = pend.solve([9, -21], 1*10**-4, 2)
# t13, y13 = pend.solve([10, -40], 1*10**-4, 2)
# t14, y14 = pend.solve([-10, 40], 1*10**-4, 2)
# t15, y15 = pend.solve([0, -40], 1*10**-4, 2)
# t16, y16 = pend.solve([math.pi-.01, -2.3], 1*10**-4, 2)


########### Problem 5: Modulo   ##############
# # for i in range(0, len(y)):
# #     y[i] = [y[i][j] % (2*math.pi) for j in range(0, len(y[i]))]


# y[0] = [(y[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y[0]))]     # mod 2pi
# y2[0] = [(y2[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y3[0] = [(y3[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# # y5[0] = [(y5[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y6[0] = [(y6[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y7[0] = [(y7[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y8[0] = [(y8[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y10[0] = [(y10[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y11[0] = [(y11[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y12[0] = [(y12[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y13[0] = [(y13[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y14[0] = [(y14[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y15[0] = [(y15[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
# y16[0] = [(y16[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y2[0]))]     # mod 2pi
#
pylab.grid()
pylab.scatter(y[0], y[1], c='#7F7F7F', lw=0, s=1)
# pylab.scatter(y2[0], y2[1], color='blue', lw=0, s=1)
# pylab.scatter(y3[0], y3[1], color='purple', lw=0, s=1)
# # pylab.scatter(y5[0], y5[1], color='green', lw=0, s=1)
# pylab.scatter(y6[0], y6[1], color='cyan', lw=0, s=1)
# pylab.scatter(y8[0], y8[1], color='orange', lw=0, s=1)
# pylab.scatter(y10[0], y10[1], color='green', lw=0, s=1)
# pylab.scatter(y11[0], y11[1], color='magenta', lw=0, s=1)
# pylab.scatter(y12[0], y12[1], color='red', lw=0, s=1)
# pylab.scatter(y13[0], y13[1], color='gray', lw=0, s=1)
# pylab.scatter(y14[0], y14[1], color='yellow', lw=0, s=1)
# pylab.scatter(y15[0], y15[1], color='teal', lw=0, s=1)
# pylab.scatter(y16[0], y16[1], color='pink', lw=0, s=1)

pylab.xlabel('Theta')
pylab.ylabel('omega')
# pylab.xlim(-0.5, 6.5)
pylab.show()

####### Problem 6 ###############
# t, y = pend.solve([2, 0], .0001, 64)
# y[0] = [(y[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y[0]))]     # mod 2pi
# print len(y[0]), len(y[1])
# pylab.grid()
# pylab.scatter(y[0][200000:], y[1][200000:], c='#7F7F7F', lw=0, s=1)
# pylab.title('A Value:' + str(A))
# pylab.xlabel('Theta')
# pylab.ylabel('omega')
# pylab.show()


######### PROBLEM 7 ############
# for i in [.0001]:        #  .1, .05, .01, .001, .0001]:
#     t_step = i
#     A = 8.4
#     t, y = pend.solve([2, 0], t_step, 60)
#     print len(y[0]), len(y[1])
#     y[0] = [(y[0][j] - math.pi) % (2*math.pi) for j in range(0, len(y[0]))]     # mod 2pi
#     pylab.grid()
#     pylab.scatter(y[0][450000:], y[1][450000:], c='#3F3F3F', lw=0, s=1)
#     pylab.title('A_value_nT:' + str(A))
#     pylab.xlabel('Theta')
#     pylab.ylabel('omega')
#     pylab.savefig(r'hw4_p6/A_value_nT:' + str(A) + '.png')
#     pylab.close()