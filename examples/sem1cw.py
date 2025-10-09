import numpy as np
from typing import Tuple
from numpy.typing import NDArray
from src.types import Data, Task

# type the formulas for the x and y components of the vector fields
def v1(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x, (1 - x)*y

def v2(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return 0.01*(x**2 + y**2), 0.01*x*y

def v3(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return y*(1 + x**2 + y**2), x*(1 - x**2 - y**2)

def v4(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), np.exp(-np.pi*x)*np.sin(np.pi*x) - y

def v5(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return y, x

def v6(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), x*y - y**2

def v7(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x, (1 - 2*x**2)*y

def v8(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x + 2*np.sqrt(x*y), y

def v9(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return y**2 - x**2, 2*x*y

def v10(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return x, (1 + x)*y + np.exp(x)*x**2

def v11(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), 1 - np.exp(y)

def v12(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return np.ones_like(x), y + y**3

ex1 = Data(
    vector_field=v1,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.25)
    ],
    y_label="z"
)

ex2 = Data(
    vector_field=v2,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.3),
        Task("zeros")
    ],
    y_label="z"
)

ex3 = Data(
    vector_field=v3,
    x_seg=(-1.4, 1.4),
    x_res=25,
    y_seg=(-1.4, 1.4),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.275),
        Task("zeros")
    ]
)

ex4 = Data(
    vector_field=v4,
    x_seg=(-2, 4),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.3)
    ],
    x_label="x/pi",
    y_label="y'"
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
    ],
    x_label="y",
    y_label="z"
)

ex6 = Data(
    vector_field=v6,
    x_seg=(-4, 4),
    x_res=25,
    y_seg=(-4, 4),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.25),
    ]
)

ex7 = Data(
    vector_field=v7,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.5),
    ],
    y_label="z"
)

ex8 = Data(
    vector_field=v8,
    x_seg=(0, 4),
    x_res=25,
    y_seg=(0, 4),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.3),
    ],
    y_label="z"
)

ex9 = Data(
    vector_field=v9,
    x_seg=(-4, 4),
    x_res=25,
    y_seg=(-4, 4),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.3),
        Task("zeros")
    ]
)

ex10 = Data(
    vector_field=v10,
    x_seg=(-4, 4),
    x_res=25,
    y_seg=(-4, 4),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.4),
        Task("zeros")
    ],
    x_label="y",
    y_label="z"
)

ex11 = Data(
    vector_field=v11,
    x_seg=(-4, 4),
    x_res=25,
    y_seg=(-4, 4),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.1)
    ]
)

ex12 = Data(
    vector_field=v12,
    x_seg=(-4, 4),
    x_res=25,
    y_seg=(-4, 4),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.25),
    ]
)

ex_list = [ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10, ex11, ex12]
