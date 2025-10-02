import numpy as np
from typing import Tuple
from numpy.typing import NDArray
from src.types import Data, Task

# type the formulas for the x and y components of the vector fields

def v2(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x, x + y

def v3(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), x + y**3

def v4(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), np.cbrt(y)

ex2 = Data(
    vector_field=v2,
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

ex3 = Data(
    vector_field=v3,
    x_seg=(-5, 5),
    x_res=25,
    y_seg=(-5, 5),
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
        Task("streamplot", density=0.25)
    ]
)


ex_list = [ex2, ex3, ex4]
