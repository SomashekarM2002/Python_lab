import matplotlib.pyplot as plt
import numpy as np

colors =['red','orange','yellow','green','blue','indigo','violet']

fig, ax =plt.subplots()

fig.patch.set_facecolor('skyblue')
ax.set_facecolor('skyblue')

for i,color in enumerate(colors):
    radius = 10-i
    theta = np.linspace(0,np.pi,100)
    x = radius*np.cos(theta)
    y = radius*np.sin(theta)
    ax.plot(x,y,color=color,linewidth=15)

ax.set_aspect('equal')
ax.axis('off')
plt.title('Rainbow plot',fontsize=20,color='darkblue')
plt.show()