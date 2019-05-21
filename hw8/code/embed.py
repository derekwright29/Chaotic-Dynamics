
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import math

data2 = open("../ps8data/data2")
data3 = open("../ps8data/data3")

data = [i for i in data3.read().split()]

thetas = [data[i] for i in range(0,len(data),2)]
thetas = [(float(i) % (2*math.pi)) for i in thetas]
times = [data[i] for i in range(1, len(data),2)]


def embed(tau, m, data_x, data_t):
    data_tau = float(data_t[1]) - float(data_t[0])
    tau = int(tau // data_tau)               #convert tau to units of data_tau, for proper indexing.
    assert(len(data_x) == len(data_t))
    reconstr_points = []

    t = data_t[0]
    for i in range(len(data_x)-m*tau):
        new_pt = []
        for k in range(m):
            new_pt.append(data_x[i+k*tau])
        reconstr_points.append(new_pt)

    return reconstr_points
# 0.01, 0.15,0.5,1,
taus = [0.02]
for t in taus:
    rec = embed(t, 7, thetas, times)
    print len(rec)


    x0, x1, x2, x3, x4, x5, x6 = zip(*rec)

    fig = plt.figure(figsize=(12,7))
    fig.set_size_inches(12.5, 6.5)
    plt.grid()
    #ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(x0, x1, z, zdir='z', s=1, lw=0)
    plt.scatter(x0, x5, s=1, lw=0 )#33c = '#7F7F7F')
    # ax.scatter(y_o[0], y_o[1], y_o[2], zdir='z', s=1, lw=0, c='#7F3333')
    #
    plt.xlabel('X')
    plt.ylabel('X+5tau')

    # eleva = 5
    # azimu = 0
    # ax.view_init(elev=eleva, azim=azimu)
    plt.title("Embedding Data3: Tau =" + str(t) + "; m=7")
    plt.savefig('Embedding_data3_05;tau=' + str(t)+'.png', dpi=500)

    plt.close()

