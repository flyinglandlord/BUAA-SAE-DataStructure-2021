import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import seaborn as sns
from scipy import interpolate

avl_data = open("btree_comb.txt", "r")
points = avl_data.readlines()
px = []
py = []
pt = []

for d in points:
    tmp_list = d.strip().split()
    px.append(float(tmp_list[0]))
    py.append(float(tmp_list[1]))
    pt.append(float(tmp_list[2]))

x_new = np.array(px)
y_new = np.array(py)
t_new = np.array(pt)

print(len(px), len(py), len(pt))

fig = plt.figure(dpi=500, figsize=(12,12))
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x_new, y_new, t_new, cmap=cm.coolwarm)
plt.tight_layout()
plt.savefig('btree_analyse.png',dpi=600) # Save
plt.show()
