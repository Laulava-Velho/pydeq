import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from numpy.typing import NDArray
from src.plotting import plot_dynamics, plot_fixed_points, make_grid

# type the formulas for the x and y components of the vector fields
def V(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return  np.ones_like(x), y**2 / (1. + x**2)

if __name__ == "__main__":

    grid = make_grid()

    fig, ax = plt.subplots()
    ax.grid()

    plot_dynamics(ax, V, grid)
    plot_fixed_points(ax, V)

    ax.set_aspect('equal')
    plt.show()
