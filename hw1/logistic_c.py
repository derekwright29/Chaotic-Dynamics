import matplotlib.pyplot as plt

def logistic_c(x0, R, m):
    """
        Third part returns the second next state of the system, xn_2
        as a function of current state, xn

    """
    cur_state = x0
    xn = [cur_state]
    xn_2 = []
    n = range(1,m+1)
    for i in n:

        next_state = cur_state * R * (1 - cur_state)
        if i != m and i != m-1:
            xn.append(next_state)
        if i != 1:
            xn_2.append(next_state)
        cur_state = next_state

    plt.grid(True)
    plt.scatter(xn, xn_2, s=20,lw=0)
    plt.title("X0 = " + str(x0) + "; R = " + str(R) + "; m = " + str(m))
    plt.xlabel("x_n")
    plt.ylabel("x_n+2")


    return xn_2, xn
