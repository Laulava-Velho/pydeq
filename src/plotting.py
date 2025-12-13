import numpy as np
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

    ax.scatter(zero_x, zero_y, color='red', marker='o', label='Zeros', zorder=3)

def plot_directionfield(ax: Axes, data: Data) -> None:

    x, y, vx, vy = data.normalized_vector_field()

    ax.quiver(x, y, vx, vy, color='blue', headwidth=0, headlength=0, headaxislength=0, pivot='mid', units='xy', minlength=1.0)
    ax.scatter(x, y, color='blue', marker='o', s=10.0, alpha=1.)

def plot_vectorfield(ax: Axes, data: Data) -> None:

    x, y, vx, vy = data.vector_field()

    task_dict = data.get_task('vectorfield').dict
    multiplier = task_dict.get('multiplier', None)
    limiter = task_dict.get('limiter', None)
    compressor = task_dict.get('compressor', None)
    color = task_dict.get('color', 'blue')
    scale = task_dict.get('scale', 5)
    width = task_dict.get('width', 0.0015)
    headwidth = task_dict.get('headwidth', 4)
    headlength = task_dict.get('headlength', 10)
    headaxislength = task_dict.get('headaxislength', 5)
    units = task_dict.get('units', 'xy')

    if compressor is not None and 1 > compressor > 0:
        norm = np.sqrt(vx**2 + vy**2)
        m = np.max(norm)
        if m != 0:
            beta = -compressor
            with np.errstate(divide='ignore'):
                reg = np.tanh(norm, out=np.ones_like(norm), where=norm != 0)
            beta_matrix = np.power(reg, beta)
            vx *= beta_matrix
            vy *= beta_matrix

    if limiter is not None and 1 >= limiter > 0:
        norm = np.sqrt(vx**2 + vy**2)
        m = np.max(norm)
        if m != 0:
            alpha = limiter * m
            with np.errstate(divide='ignore'):
                reg = np.tanh(alpha / norm, out=np.ones_like(norm), where=norm != 0)
            vx *= reg
            vy *= reg

    if multiplier is not None:
        vx *= multiplier
        vy *= multiplier

    ax.quiver(x, y, vx, vy, color=color, scale=scale, width=width, headwidth=headwidth, headlength=headlength, headaxislength=headaxislength, units=units)
