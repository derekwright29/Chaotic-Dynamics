import matplotlib.pyplot as plt


fn_data = open("../TiseanOuts/fn_data2_f250.txt")

data = [i for i in fn_data.read().split()]
dat = [float(data[i]) for i in range(1, len(data), 4)]
print data[:10]
print dat[:10]

#
# # def find_min(data):
# #     temp = float("Inf")
# #     i=0
# #     while temp >= data[i]:
# #         temp = data[i]
# #         i += 1
# #
# #     print i
# #
# # find_min(dat)
#
#
print(len(dat))
x = range(len(dat))

pt_ones = [.1,.1,.1,.1,.1,.1,.1,.1,.1,.1]
# print x[:10]
# print "Minima?", dat[150:170]
# print dat[156]

fig = plt.figure(figsize=(12,7))
fig.set_size_inches(12.5, 6.5)
#plt.grid()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(x0, x1, z, zdir='z', s=1, lw=0)
plt.plot(x, dat, '-o' )#33c = '#7F7F7F')
plt.plot(x, pt_ones, '-b',  )#33c = '#7F7F7F')
# ax.scatter(y_o[0], y_o[1], y_o[2], zdir='z', s=1, lw=0, c='#7F3333')
#
plt.xlabel('dimension')
plt.ylabel('ration of false nearest neighbors')

# eleva = 5
# azimu = 0
# ax.view_init(elev=eleva, azim=azimu)
plt.title("Finding m")
plt.savefig('txFinding_m.png', dpi=500)
plt.show()
plt.close()