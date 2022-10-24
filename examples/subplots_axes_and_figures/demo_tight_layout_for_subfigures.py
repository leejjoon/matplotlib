"""
=============================================
Resizing axes in Subfigures with tight layout
=============================================

`~.Subfigure.tight_layout` is similar to `~.Fgure.tight_layout` but is
applied toa subfigure.

See :doc:`/tutorials/intermediate/tight_layout_guide` for more details.

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

available = [t for t in plt.style.available if not t.startswith("_")][:9]


gridspec = GridSpec(3, 3)

x = np.arange(-2, 8, .1)
y = .1 * x ** 3 - x ** 2 + 3 * x + 2

fig = plt.figure(num=1)

# tight_layout is called for each subfigure, thus subplots in each
# subfigure are resizedadjusted independently. However, note that
# subfigures share ``SubplotParams` of the parent figure and there
# could be unwanted sideeffects.

for i, style in enumerate(available):
    with plt.style.context(style):
        sfig = fig.add_subfigure(gridspec[i])
        ax = sfig.add_subplot(111)
        ax.plot(x, y)
        ax.set_title(style)
        sfig.tight_layout(pad=0.5)


fig = plt.figure(num=2)

# We use new `TightLayoutSubfiguresEngine`. It creates a sinle `SubplotParams`
# combining parameters of each Subplots which are used by all Subfigures.

for i, style in enumerate(available):
    with plt.style.context(style):
        sfig = fig.add_subfigure(gridspec[i])
        ax = sfig.add_subplot(111)
        ax.plot(x, y)
        ax.set_title(style)

from matplotlib.layout_engine import TightLayoutSubfiguresEngine
engine = TightLayoutSubfiguresEngine(pad=0.5)
fig.set_layout_engine(engine)

plt.show()
