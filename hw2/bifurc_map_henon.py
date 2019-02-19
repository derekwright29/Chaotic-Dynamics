import matplotlib.pyplot as plt
import numpy as np


def henon_a_b(x0, x1, a, b, k):

    """
        Calculates the iterates xn and yn based on the Henon map

    """
    cur_x_1 = x0
    cur_x0 = x1
    xn = [cur_x_1, cur_x0]

    n = range(0, k+1)
    for i in n[2::]:
        next_x = xn[i-2]*b + 1 - a*(xn[i-1])**2
        xn.append(next_x)

    return xn, n


def bifurc_map(x0, x1, al, ah, b, m, l):

    astep = .0005
    X_N = []
    A = []
    As = [x*astep + al for x in range(0, int((ah-al)/astep))]

    j = 0
    for a in As:

        xn, _n = henon_a_b(x0, x1, a, b, m)
        xn = xn[l::]
        xn = [i for i in xn]
        X_N.append(xn)
        A.append([a]*(m-l+1))

        j = j + 1
    fig = plt.figure(figsize=(20, 10))
    for q in range(0, len(A)):
        plt.scatter(A[q], X_N[q], color='#7F7F7F', marker='o', s=(72./fig.dpi)**2, lw=0)

    plt.title("Henon Bifurcation Plot")
    plt.xlabel("A")
    plt.ylabel("x_n")
    # plt.ylim(-.2, 0)
    plt.show()


bifurc_map(.1, .1, 0, 1.4, 0.3, 1000, 700)







