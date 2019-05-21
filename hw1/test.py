from logistic_a import logistic_a as la
from logistic_b import logistic_b as lb
from logistic_c import logistic_c as lc
import matplotlib.pyplot as plt


def test_helper(x0, R, m):
    # Part a
    plt.rc('axes', axisbelow=True)
    plt.figure(1)
    states, time = la(x0, R, m)
    print states, time

    # Part b
    plt.figure(2)
    states, next_states = lb(x0, R, m)
    print states, next_states

    # Part c
    plt.figure(3)
    states, next2states = lc(x0, R, m)
    print states, next2states
    plt.show()

m = 500
arr = [

(.5, 3.5, m)]


for i in arr:
    test_helper(i[0], i[1], i[2])


