import numpy as np
from typing import Tuple
from numpy.typing import NDArray
from src.types import Data, Task

# type the formulas for the x and y components of the vector fields
def v1(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x + y, x - y

def v2(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return -2*y, 1 - 3*x**2

def v3(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return 0.1*np.ones_like(x), (y**3 - y)/2

def v4(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return y, -x

def v5(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return 0.1*y, (y**3 - y)/2

ex1 = Data(
    vector_field=v1,
    x_seg=(-2, 2),
    x_res=25,
    y_seg=(-2, 2),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.5),
        Task("zeros")
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
        Task("streamplot", density=0.3)
    ]
)

ex3 = Data(
    vector_field=v3,
    x_seg=(-0.5, 0.5),
    x_res=25,
    y_seg=(0, 1),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.3)
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
        Task("streamplot", density=0.15),
        Task("zeros")
    ]
)

ex5 = Data(
    vector_field=v5,
    x_seg=(-0.5, 0.5),
    x_res=25,
    y_seg=(0, 1),
    y_res=25,
    tasks=[
        Task("vectorfield"),
        Task("streamplot", density=0.3)
    ]
)

ex_list = [ex1, ex2, ex3, ex4, ex5]
