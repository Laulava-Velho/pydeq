import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from numpy.typing import NDArray
from src.run_utils import run, save_plot
from src.types import Data, Task

# type the formulas for the x and y components of the vector fields
def v1(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), x*y

def v2(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return  np.ones_like(x), y**2 / (1. + x**2)

def v3(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), y*(1. - y / 4.0)

def v4(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return 1. + np.exp(y), x

def v5(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x, x + y

def v6(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return 5*x**2, 5*(2*x*y - y**2)

ex1 =Data(
    vector_field=v1,
    x_seg=(-2, 2),
    x_res=25,
    y_seg=(-2, 2),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.4)
    ]
)

ex2 = Data(
    vector_field=v2,
    x_seg=(-4, 4),
    x_res=25,
    y_seg=(-4, 4),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.5)
    ]
)

ex3 = Data(
    vector_field=v3,
    x_seg=(-4, 4),
    x_res=25,
    y_seg=(0, 8),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.2)
    ]
)

ex4 = Data(
    vector_field=v4,
    x_seg=(-4, 4),
    x_res=25,
    y_seg=(-4, 4),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.2)
    ]
)

ex5 = Data(
    vector_field=v5,
    x_seg=(-4, 4),
    x_res=25,
    y_seg=(-4, 4),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.2),
        Task("zeros")
    ]
)

ex6 = Data(
    vector_field=v6,
    x_seg=(0, 4),
    x_res=25,
    y_seg=(-2, 2),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.25),
        Task("zeros")
    ]
)

ex_list = [ex1, ex2, ex3, ex4, ex5, ex6]

if __name__ == "__main__":

    for data in ex_list:
        fig, ax = plt.subplots(figsize=(16 , 12))
        ax.grid()
        run(ax, data)
        ax.set_aspect('equal')
        plt.show()
        save_plot(fig)

    print("Thank you for using the program.")
