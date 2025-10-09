import numpy as np
from typing import Tuple
from numpy.typing import NDArray
from src.types import Data, Task

# type the formulas for the x and y components of the vector fields
def v1(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return y, 3*y - 2*x

ex1 = Data(
    vector_field=v1,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.25),
        Task("zeros")
    ],
    y_label="dy/dx",
    x_label="y"
)

def v2(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return y, 4*y - 13*x

ex2 = Data(
    vector_field=v2,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.25),
        Task("zeros")
    ],
    y_label="dy/dx",
    x_label="y"
)

def v3(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    omega_sqr = 1
    return y, -omega_sqr*x

ex3 = Data(
    vector_field=v3,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.2),
        Task("zeros")
    ],
    y_label="dy/dx",
    x_label="y"
)

def v4(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return y, -6*y - 9*x

ex4 = Data(
    vector_field=v4,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.25),
        Task("zeros")
    ],
    y_label="dy/dx",
    x_label="y"
)

ex_list = [ex1, ex2, ex3, ex4]
