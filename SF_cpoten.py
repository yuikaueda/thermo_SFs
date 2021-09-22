import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 10, 100)
y = -2/(1+np.exp(-x))+3

fig, ax = plt.subplots(1, 1)

plt.ylim([1,3])
plt.xlim([0,5])

ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])

ax.set_yticks([0,1,2])
ax.set_yticklabels(['0','$\mu_{SF} ^{c}$','$\mu_{SF} ^{0}$'])

plt.xlabel('F', fontsize=20)
plt.ylabel('$\mu_{SF}$', fontsize=20)
ax.plot(x,y,color='black')

plt.show()
fig.savefig("SF_cpote_fig.png",bbox_inches="tight")
