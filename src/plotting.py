import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Tuple
from numpy.typing import NDArray

def plot_dynamics(vector_field: Callable[[NDArray, NDArray], Tuple[NDArray, NDArray]],
    x_left: int = -2, x_right: int = 4, x_res: int = 100, y_down: int = -4, y_up: int = 2, y_res: int = 100) -> None:

    x, y = np.meshgrid(np.linspace(x_left, x_right, x_res), np.linspace(y_down, y_up, y_res))

    vx, vy = vector_field(x, y)

    if type(vx) != object:
        vx = vx * np.ones(x.shape, dtype=float)
    if type(vy) != object:
        vy = vy * np.ones(x.shape, dtype=float)

    fig, ax = plt.subplots()
    plt.grid()
    ax.streamplot(x, y, vx, vy)
    ax.set_aspect('equal')
    plt.show()
