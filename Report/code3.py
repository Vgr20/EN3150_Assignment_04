def mappingKernel (x1,x2) :
    return x1**2,x2**2,x1*x2


mappedx_2 ,mappedy_2 ,mappedz_2 = mappingKernel (X [:, 0], X [:, 1])

# visualize in 3D

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure ()
ax = fig.add_subplot (111 , projection ='3d')
ax.scatter (mappedx_2 ,mappedy_2 ,mappedz_2 , c=y, cmap=plt.cm.Paired)
plt.show()
