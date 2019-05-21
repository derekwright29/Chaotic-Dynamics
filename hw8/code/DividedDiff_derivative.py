import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import math
from numpy import diff
import pdb

file = open("../ps8data/data1")

data = [float(i) for i in file.read().split()]
thetas = [data[i] for i in range(0,len(data),2)]
times = [(data[i]% (2*math.pi)) for i in range(1, len(data),2)]

DWN_SMPL_VAL = [1,2,3,4,5,6,7,8,9,10,11,12]
for s in DWN_SMPL_VAL:
    dwn_thetas = [(thetas[i]) for i in range(0, len(thetas),s)]
    dwn_times = [times[i] for i in range(0,len(times), s)]

    omegas = []
    for i in range(len(dwn_thetas)-1):
        # if i == 200:
            # pdb.set_trace()
        omegas.append((dwn_thetas[i+1]-dwn_thetas[i])/(dwn_times[i+1] - dwn_times[i]))

    # omegas = diff(dwn_thetas)/diff(dwn_times)
    print omegas

    fig = plt.figure()
    plt.grid()
    plt.scatter(dwn_thetas[1:], omegas, s=3, lw=0)
    plt.xlabel('Theta')
    plt.ylabel('Omega (divided difference)')
    plt.title("Reconstructed Trajectory: Downsampling: " + str(s))
    #plt.xlim(math.pi - .5, math.pi + 0.5)
    plt.ylim(-2,2)

    plt.savefig("Divided_Diff_1a;dwnsmpl-"+str(s)+".png", dpi=400)
    plt.close()
