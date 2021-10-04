import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.8e-6, 1000)
y = 1.0e-6*(x - 1.4e-6)*(x - 1.4e-6)

fig, ax = plt.subplots(1, 1)

#plt.ylim([0,])
#plt.xlim([0,])

ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])

#ax.set_yticks([0,])
#ax.set_yticklabels(['0','$F_all$'], fontsize=18)
#ax.set_xticks([6])
#ax.set_xticklabels(['$l_0$'], fontsize=18)

#plt.xlim([0,2e-6])
plt.ylabel('Gibbs free energy $G$',fontsize=20)
plt.xlabel(r'Extent of reaction $\zeta$',fontsize=20)

ax.plot(x,y,color='black')
plt.show()
fig.savefig("tension_force.png",bbox_inches="tight")
