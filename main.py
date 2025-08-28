import numpy as np
from typing import Tuple
from numpy.typing import NDArray
from src.plotting import plot_dynamics

# type the formulas for the x and y components of the vector fields
def V(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return  np.ones_like(x), y**2 / (1. + x**2)

if __name__ == "__main__":
    plot_dynamics(V)
