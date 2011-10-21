
from matplotlib.axes import subplot_class_factory

class ProjectionBase(object):
    """
    The subplot command can take a projection parameter. It could be a
    string, or the instance of the ProjectionBase class.

    subclass must overload the 'get_axes_class_arguments' method.
    """

    def get_axes_class_arguments(self):
        raise NotImplementedError

    def isinstance(self, ax):
        axes_class, axes_kwargs = self.get_axes_class_arguments()
        return isinstance(ax, axes_class)

    def get_axes(self, fig, rect, **kwargs):
        axes_class, axes_kwargs = self.get_axes_class_arguments()
        kwargs.update(axes_kwargs)
        ax = axes_class(fig, rect, **kwargs)
        return ax

    def get_subplot(self, fig, *args, **kwargs):
        axes_class, axes_kwargs = self.get_axes_class_arguments()
        kwargs.update(axes_kwargs)
        ax = subplot_class_factory(axes_class)(fig, *args, **kwargs)
        return ax


class Projection(object):

    def __init__(self, axes_class, axes_kwargs):
        self._axes_class = axes_class
        self._axes_kwargs = axes_kwargs

    def get_axes_class_arguments(self):
        return self._axes_class, self._axes_kwargs
