import numpy as np
from typing import Tuple
from numpy.typing import NDArray
from src.types import Data, Task

# type the formulas for the x and y components of the vector fields
def v3(x: NDArray, y: NDArray) -> Tuple[NDArray, NDArray]:
    return 2*x, 2*y

ex3 = Data(
    vector_field=v3,
    x_seg=(-3, 3),
    x_res=25,
    y_seg=(-3, 3),
    y_res=25,
    tasks=[
        Task("directionfield"),
        Task("streamplot", density=0.25)
    ]
)

ex_list = [ex3]
