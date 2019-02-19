import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 2))

print fig.dpi


Rh = 4
Rl = 2.8
rstep = .01

test = int((Rh-Rl)/rstep)


print test