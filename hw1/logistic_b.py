import matplotlib.pyplot as plt

def logistic_b(x0, R, m):
    """
        Second part returns the next state of the system, xn_1 as a function of current state xn

    """
    cur_state = x0
    xn = [cur_state]
    xn_1 = []
    n = range(1,m+1)
    for i in n:

        next_state = cur_state * R * (1 - cur_state)
        if i != m:
            xn.append(next_state)
        xn_1.append(next_state)
        cur_state = next_state

    plt.grid(True)
    plt.scatter(xn, xn_1, s=10,lw=0)
    plt.title("X0 = " + str(x0) + "; R = " + str(R) + "; m = " + str(m))
    plt.xlabel("x_n")
    plt.ylabel("x_n+1")


    return xn_1, xn
