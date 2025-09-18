import numpy as np
from typing import Tuple
from numpy.typing import NDArray
from src.types import Data, Task

# type the formulas for the x and y components of the vector fields
def v1(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), y*x**2

def v2(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x, -(x + 1)*y + 3*x**2*np.exp(-x)

def v3(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), -y + 1/(1 + np.exp(x))

def v4(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x*np.log(x, where=x>0), 2*y + np.log(x, where=x>0)

def v5(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return 2*x + y**3, y

def v6(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), -y + np.exp(x)*y**2

ex1 = Data(
    vector_field=v1,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.25)
    ]
)

ex2 = Data(
    vector_field=v2,
    x_seg=(-2, 2),
    x_res=25,
    y_seg=(-2, 2),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.4),
        Task("zeros")
    ]
)

ex3 = Data(
    vector_field=v3,
    x_seg=(-5, 5),
    x_res=25,
    y_seg=(-5, 5),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.3)
    ]
)

ex4 = Data(
    vector_field=v4,
    x_seg=(0, 4),
    x_res=25,
    y_seg=(-2, 2),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.3),
        Task("zeros", x0=[1, 0])
    ]
)

ex5 = Data(
    vector_field=v5,
    x_seg=(-2, 2),
    x_res=25,
    y_seg=(-2, 2),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.25),
        Task("zeros")
    ]
)

ex6 = Data(
    vector_field=v6,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.2),
    ]
)

ex_list = [ex1, ex2, ex3, ex4, ex5, ex6]
