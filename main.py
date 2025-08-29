import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from numpy.typing import NDArray
from src.plotting import (plot_dynamics, plot_fixed_points, make_grid, plot_directionfield)

# type the formulas for the x and y components of the vector fields
def V(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return  np.ones_like(x), y**2 / (1. + x**2)

if __name__ == "__main__":

    grid = make_grid(x_res=25, y_res=25)

    fig, ax = plt.subplots(figsize=(16 , 12))
    ax.grid()

    plot_dynamics(ax, V, grid, density=1., minlength=1.0)
    plot_directionfield(ax, V, grid)
    # plot_fixed_points(ax, V)

    ax.set_aspect('equal')
    plt.show()

    print("Do you want to save the plot? [yes|no]")
    answer = input().lower()
    if answer == "yes":
        print("Enter the file name:")
        filename = input()
        fig.savefig(filename+'.svg', format='svg')
    else:
        print("Okay, plot not saved.")

    print("Thank you for using the program.")
