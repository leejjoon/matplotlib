from matplotlib.hatch import CustomHatchPatternBase
from matplotlib.path import Path

import mpl_pe_pattern_usgs

class USGSPattern(CustomHatchPatternBase):
    _pattern_usgs = mpl_pe_pattern_usgs.PatternUSGS()

    def __init__(self, pid):
        p = self._pattern_usgs.get(pid)
        self._p = Path(p.path.vertices / p.width, p.path.codes)

    def get_path(self):
        return self._p
