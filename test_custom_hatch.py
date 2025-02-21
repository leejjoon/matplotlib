import matplotlib.pyplot as plt


fig, ax = plt.subplots(1, 1, layout='constrained', figsize=(3.2, 3.2),
                       clear=True, num=1)

from hatch_usgs import USGSPattern
ax.patch.set_hatch(USGSPattern("605"))

# ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch="/"))
# ax.axis('equal')
# ax.axis('off')

