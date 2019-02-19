import matplotlib.pyplot as plt
import numpy as np

def logistic_a(x0, R, m):

    """
        First part returns the current state of the system, xn as a function of time, n

    """
    cur_state = x0
    xn = [cur_state]
    n = range(0,m+1)
    for i in n[1::]:

        next_state = cur_state * R * (1 - cur_state)    # logistic equation
        xn.append(next_state)
        cur_state = next_state

    return xn, n


def bifurc_map(x0, Rl, Rh, m, l):

    rstep = .0005
    X_N = []
    R = []
    Rs = [x*rstep + Rl for x in range(0, int((Rh-Rl)/rstep))]

    j = 0
    for r in Rs:

        xn, _n = logistic_a(x0, r, m)
        xn = xn[l::]
        xn = [i for i in xn]
        X_N.append(xn)
        R.append([r]*(m-l+1))

        j = j + 1
    fig = plt.figure(figsize=(20, 10))
    for q in range(0, len(R)):
        plt.scatter(R[q], X_N[q], c='#7F7F7F', s=(72./fig.dpi)**2, lw=0)

    plt.show()


bifurc_map(.1, 2.8, 4, 10000, 9700)







