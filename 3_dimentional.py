import scipy.stats as stats
from matplotlib import pyplot as plt

from mpl_toolkits import mplot3d
import numpy as np

z=stats.multivariate_normal.rvs([2 ,2 ,2],
                     [[4,3,2],[3,8,4],[2,4,9]],10000) 


#Génération d'un plan en 3d pour afficher les triplet generer précédement
fig = plt.figure(figsize = (10, 7))
ax= plt.axes(projection ="3d")
ax.scatter3D(z[:,0], z[:,1], z[:,2], color = "red")
plt.show()