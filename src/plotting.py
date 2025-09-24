from .types import Data
from matplotlib.axes import Axes
from scipy.optimize import fsolve

def plot_streamplot(ax: Axes, data: Data) -> None:

    x, y, vx, vy = data.vector_field()

    kwargs = {
        'minlength': .0,
        'maxlength': 5.0,
        'arrowstyle': '-',
        'color': 'green',
        'integration_direction': 'both',
        'broken_streamlines': False,
        'density': 1.0
    }
    task_dict = data.get_task('streamplot').dict
    kwargs.update((k, task_dict[k]) for k in kwargs.keys() & task_dict.keys())

    ax.streamplot(x, y, vx, vy, **kwargs)

def plot_zeros(ax: Axes, data: Data) -> None:

    wrapped_vf = data.wrapped_vf

    task_dict = data.get_task('zeros').dict
    x0 = task_dict.get('x0', [0, 0])

    zero, _, _, _ = fsolve(wrapped_vf, x0, full_output=True)
    zero_x, zero_y = zero[0], zero[1]

    ax.scatter(zero_x, zero_y, color='red', marker='o', label='Zeros')

def plot_directionfield(ax: Axes, data: Data) -> None:

    x, y, vx, vy = data.normalized_vector_field()

    ax.quiver(x, y, vx, vy, color='blue', headwidth=0, headlength=0, headaxislength=0, pivot='mid', units='xy', minlength=1.0)
    ax.scatter(x, y, color='blue', marker='o', s=10.0, alpha=1.)

def plot_vectorfield(ax: Axes, data: Data) -> None:

    x, y, vx, vy = data.vector_field()

    ax.quiver(x, y, vx, vy, color='blue', scale=5, width=0.0015, headwidth=4, headlength=10, headaxislength=5, units='xy')
