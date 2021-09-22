import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

R = 8.31
T = 309.65

f_0 = 0.0
f_1 = 1.0
f_2 = 2.0
f_3 = 3.0

mub_0 = -2000/(1+np.exp(-f_0))+1000
mub_1 = -2000/(1+np.exp(-f_1))+1000
mub_2 = -2000/(1+np.exp(-f_2))+1000
#mua_3 = -2000/(1+np.exp(-f_3))+1000

#print(mua_0)

mua = 1.0

x = np.linspace(0, 1, 100)
y0 = (1.0-x)*mua + x*mub_0 + (1.0-x)*R*T*np.log(1.0-x) + x*R*T*np.log(x)
y1 = (1.0-x)*mua + x*mub_1 + (1.0-x)*R*T*np.log(1.0-x) + x*R*T*np.log(x)
y2 = (1.0-x)*mua + x*mub_2 + (1.0-x)*R*T*np.log(1.0-x) + x*R*T*np.log(x)
#y3 = (1.0-x)*mua_3 + x*mub + (1.0-x)*R*T*np.log(1.0-x) + x*R*T*np.log(x)
#y = (1.0-x)*R*T*np.log(1.0-x) + x*R*T*np.log(x)

ax.axes.yaxis.set_ticks([])
plt.xlabel('$\zeta$', fontsize=20)
plt.ylabel('G', fontsize=20)
ax.plot(x, y0, color='red', label = r'$F_{0}$')
ax.plot(x, y1, color='forestgreen', label = r'$F_{1}$')
ax.plot(x, y2, color='steelblue', label = r'$F_{2}$')
#ax.plot(x, y3, color='dimgrey', label = r'$F_{3}$')

ax.legend(loc='best')
plt.show()
fig.savefig("G_fig.png", bbox_inches="tight")
