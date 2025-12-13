import numpy as np
from typing import Tuple
from numpy.typing import NDArray
from src.types import Data, Task

# type the formulas for the x and y components of the vector fields
def v1(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x**2 + y**2 - 2*x, 3*x**2 - x + 3*y

def v2(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.log(4*y + np.exp(-3*x)), 2*y - 1 + np.cbrt(1 - 6*x)

def v3(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return y - x + x*y, x - y - x**2 - y**3

def v4(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x*y - x**3 + y**3, x**2 - y**3

ex1 = Data(
    vector_field=v1,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("vectorfield", limiter=0.0075, multiplier=3, scale=5, width=0.0025, headwidth=8, headlength=20, headaxislength=10, units='xy'),
        Task("streamplot", density=0.3),
        Task("zeros")
    ]
)

ex2 = Data(
    vector_field=v2,
    x_seg=(-0.1, 0.1),
    x_res=25,
    y_seg=(-0.1, 0.1),
    y_res=25,
    tasks=[
        Task("vectorfield", limiter=0.01, multiplier=0.5, scale=1, width=0.00025, headwidth=4, headlength=10, headaxislength=5, units='xy'),
        Task("streamplot", density=0.3),
        Task("zeros")
    ]
)

ex3 = Data(
    vector_field=v3,
    x_seg=(-1, 1),
    x_res=25,
    y_seg=(-1, 1),
    y_res=25,
    tasks=[
        Task("vectorfield", limiter=0.015, scale=1, width=0.001, headwidth=8, headlength=20, headaxislength=10, units='xy'),
        Task("streamplot", density=0.3),
        Task("zeros")
    ]
)

ex4 = Data(
    vector_field=v4,
    x_seg=(-0.25, 0.25),
    x_res=25,
    y_seg=(-0.25, 0.25),
    y_res=25,
    tasks=[
        Task("vectorfield", limiter=0.125, compressor=0.7, multiplier=1.25, scale=5, width=0.00075, headwidth=4, headlength=10, headaxislength=5, units='xy'),
        Task("streamplot", density=0.25),
        Task("zeros")
    ]
)

ex_list = [ex1, ex2, ex3, ex4]
