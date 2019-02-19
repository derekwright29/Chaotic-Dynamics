from logistic_a import logistic_a as la
from logistic_b import logistic_b as lb
from logistic_c import logistic_c as lc
import matplotlib.pyplot as plt


def test_helper(x0, R, m):
    # Part a
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


arr = [(.2, 2, 6),
       (.01, 2, 10),
       (.99, 2, 10),
       (.200001, 2, 7),
       (.2, 3.3, 6),
       (.2, 3.6, 12),
       (.2, 3.83, 12),
       (.200001, 3.83, 14),
       (.2, 3.9, 14),
       (.2, 4.1, 14),
       (.5, 3, 12),
       (.2, 2.5, 12),
       (.200001, 2.5, 12),
       (.5, 2.5, 12),
       (.7, 2.5, 14)]


for i in arr:
    test_helper(i[0], i[1], i[2])


