import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import numpy as np



mutual_data = open("../TiseanOuts/data2_f250.txt")

data = [i for i in mutual_data.read().split()]
dat = [float(data[i]) for i in range(1, len(data), 2)]
print data[:10]
print dat[:10]

dat_arr = np.array(dat)

# for local minima
minima = argrelextrema(dat_arr, np.less)
print minima[0][0]
minima_y = dat[int(minima[0][0])]

line = [minima_y] * 500
# def find_min(data):
#     temp = float("Inf")
#     i=0
#     while temp >= data[i]:
#         temp = data[i]
#         i += 1
#
#     print i
#
# find_min(dat)


x = range(len(dat))

fig = plt.figure(figsize=(12,7))
fig.set_size_inches(12.5, 6.5)
#plt.grid()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(x0, x1, z, zdir='z', s=1, lw=0)
plt.scatter(x[70:], dat[70:], s=4, lw=0 )#33c = '#7F7F7F')
plt.plot(x[70:], line[68:],'-', linewidth=1, color='coral')
# ax.scatter(y_o[0], y_o[1], y_o[2], zdir='z', s=1, lw=0, c='#7F3333')
#
plt.xlabel('t')
plt.ylabel('correlation')

# eleva = 5
# azimu = 0
# ax.view_init(elev=eleva, azim=azimu)
plt.title("Finding Tau")
plt.savefig('txzFinding_Tau.png', dpi=500)
plt.show()
plt.close()