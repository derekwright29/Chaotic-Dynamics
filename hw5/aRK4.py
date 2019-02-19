class aRK4(object):

    def __init__(self, *functions):

        """
        Initialize a RK4 solver.
        :param functions: The functions to solve.
        """

        self.f = functions
        self.t = 0


    def solve(self, y, h, n, TOL):

        """
        Solve the system ODEs.
        :param y: A list of starting values. An initial condition
        :param h: Step size.
        :param n: Endpoint.
        :param TOL: L-infinity tolerance to change h-step
        """

        t = []
        res = []
        for i in y:
            res.append([])

        while self.t <= n and h != 0:
            t.append(self.t)
            #take full h step
            y = self._solve(y, self.t, h) # y is next point

            # Adaptive adjustments
            y2 = self._solve(y, self.t, h/2) # y2 is first half-step point
            y2 = self._solve(y2, self.t+h/2, h/2)  # y2 is overwritten to be the second half-step; update self.t+h/2 accordingly, as well as giveing the start point fo the old y2
            err = max([abs(y[i]-y2[i]) for i in range(0, len(y))])  #take L-infinity norm
            # if we are within bounds
            if err < TOL:
                for c, i in enumerate(y):
                    res[c].append(i)
                self.t += h
                if err < TOL/2:
                    h = h*2
            else:
                for c, i in enumerate(y2):
                    res[c].append(i)
                self.t += h
                h = h/2


            if self.t + h > n:
                h = n - self.t

        self._reset()
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

    def _reset(self):
        self.t = 0