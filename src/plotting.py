import numpy as np
from typing import Callable, Tuple
from matplotlib.axes import Axes
from numpy.typing import NDArray
from scipy.optimize import fsolve

def make_grid(x_left: int = -2, x_right: int = 4, x_res: int = 100, y_down: int = -4, y_up: int = 2, y_res: int = 100) -> Tuple[NDArray, NDArray]:

    x, y = np.meshgrid(np.linspace(x_left, x_right, x_res), np.linspace(y_down, y_up, y_res))

    return x, y

def normalize_field(vx: NDArray, vy: NDArray, epsilon: float = 10e-8) -> Tuple[NDArray, NDArray]:

    norms = np.sqrt(vx**2 + vy**2)
    mask = (norms <= epsilon)
    norms[mask] = 1
    vx /= norms
    vy /= norms

    return vx, vy

def plot_dynamics(ax: Axes, vector_field: Callable[[NDArray, NDArray], Tuple[NDArray, NDArray]], grid: Tuple[NDArray, NDArray],
    minlength: float = 0.1, maxlength: float = 4.0, arrowstyle: str = '-', density: float | Tuple[float, float] = 1.0) -> None:

    x, y = grid
    vx, vy = vector_field(x, y)

    ax.streamplot(x, y, vx, vy, minlength=minlength, maxlength=maxlength, arrowstyle=arrowstyle, density=density, color='green')

def plot_fixed_points(ax: Axes, vector_field: Callable[[NDArray, NDArray], Tuple[NDArray, NDArray]]) -> None:

    def my_function(arg):
        x, y = arg[0], arg[1]
        return vector_field(x, y)

    zero, _, _, _ = fsolve(my_function, [0, 0], full_output=True)
    zero_x, zero_y = zero[0], zero[1]
    ax.scatter(zero_x, zero_y, color='red', marker='o', label='Zeros')

def plot_directionfield(ax: Axes, vector_field: Callable[[NDArray, NDArray], Tuple[NDArray, NDArray]], grid: Tuple[NDArray, NDArray]) -> None:

    x, y = grid
    vx, vy = normalize_field(*vector_field(x, y))

    ax.quiver(x, y, vx, vy, color='blue', headwidth=0, headlength=0, headaxislength=0, pivot='mid', units='xy', minlength=1.0)
    ax.scatter(x, y, color='blue', marker='o', s=20, alpha=1.)
    ax.scatter(x, y, color='white', marker='o', s=12.5, alpha=1.)
