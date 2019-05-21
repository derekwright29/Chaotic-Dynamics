import matplotlib.pyplot as plt

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

    plt.grid(True)
    plt.scatter(n, xn, s=10, lw=0)
    plt.title("X0 = " + str(x0) + "; R = " + str(R) + "; m = " + str(m))
    plt.xlabel("n")
    plt.ylabel("xn")


    return xn, n

