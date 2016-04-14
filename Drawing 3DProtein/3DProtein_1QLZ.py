# draw 3D protein 1QLZ
store = []
with open("protein_1qlz.pdb") as protein:
	for lines in protein:
		if "ATOM   " in lines:
			lines = lines.split()
			#atom cordinate starts at 6
			store.append(map(float, lines[6:9]))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x, y, z = zip(*store)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(x, y, z, "o")
ax.axis("off")

plt.show()