import numpy as np
from typing import Callable, Tuple
from matplotlib.axes import Axes
from numpy.typing import NDArray
from scipy.optimize import fsolve

def make_grid(x_left: int = -2, x_right: int = 4, x_res: int = 100, y_down: int = -4, y_up: int = 2, y_res: int = 100) -> Tuple[NDArray, NDArray]:

    x, y = np.meshgrid(np.linspace(x_left, x_right, x_res), np.linspace(y_down, y_up, y_res))

    return x, y

def plot_dynamics(ax: Axes, vector_field: Callable[[NDArray, NDArray], Tuple[NDArray, NDArray]], grid: Tuple[NDArray, NDArray]) -> None:

    x, y = grid
    vx, vy = vector_field(x, y)

    if type(vx) != object:
        vx = vx * np.ones(x.shape, dtype=float)
    if type(vy) != object:
        vy = vy * np.ones(x.shape, dtype=float)

    ax.streamplot(x, y, vx, vy)

def plot_fixed_points(ax: Axes, vector_field: Callable[[NDArray, NDArray], Tuple[NDArray, NDArray]]) -> None:

    def my_function(arg):
        x, y = arg[0], arg[1]
        return vector_field(x, y)

    zero, _, _, _ = fsolve(my_function, [0, 0], full_output=True)
    zero_x, zero_y = zero[0], zero[1]
    ax.scatter(zero_x, zero_y, color='red', marker='o', label='Zeros')
