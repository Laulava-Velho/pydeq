import numpy as np
from numpy.typing import NDArray
from typing import Callable, Tuple, List

def make_grid(x_left: float | int, x_right: float | int, x_res: int, y_down: float | int, y_up: float | int, y_res: int) -> Tuple[NDArray, NDArray]:
    x, y = np.meshgrid(np.linspace(x_left, x_right, x_res), np.linspace(y_down, y_up, y_res))
    return x, y

def normalize_field(vx: NDArray, vy: NDArray, epsilon: float = 10e-8) -> Tuple[NDArray, NDArray]:

    norms = np.sqrt(vx**2 + vy**2)
    mask = (norms <= epsilon)
    norms[mask] = 1
    nvx = vx / norms
    nvy = vy / norms

    return nvx, nvy

class Task:
    def __init__(self, name: str, **kwargs):
        self.name = name
        self.dict = kwargs

class Data:

    def __init__(
        self,
        vector_field: Callable[[NDArray, NDArray], Tuple[NDArray, NDArray]],
        x_seg: Tuple[float | int, float | int],
        y_seg: Tuple[float | int, float | int],
        x_res: int,
        y_res: int,
        tasks: List[Task],
        **kwargs):

        self._vf = vector_field
        self._x_seg = x_seg
        self._y_seg = y_seg
        self._x_res = x_res
        self._y_res = y_res
        self._tasks = tasks
        self._kwargs = kwargs

        self._grid = make_grid(x_left=x_seg[0], x_right=x_seg[1], x_res=x_res, y_down=y_seg[0], y_up=y_seg[1], y_res=y_res)
        self._v = self._vf(*self._grid)

        def wrapped_vf(arg):
            x, y = arg[0], arg[1]
            return vector_field(x, y)

        self.wrapped_vf = wrapped_vf

    def vector_field(self) -> Tuple[NDArray, NDArray, NDArray, NDArray]:
        x, y = self._grid
        vx, vy = self._v
        return x, y, vx, vy

    def normalized_vector_field(self, epsilon: float = 10e-8) -> Tuple[NDArray, NDArray, NDArray, NDArray]:
        x, y = self._grid
        vx, vy = self._v
        nvx, nvy = normalize_field(vx, vy, epsilon=epsilon)
        return x, y, nvx, nvy

    def get_task(self, name: str) -> Task:
        for task in self._tasks:
            if task.name == name:
                return task
        raise ValueError(f"Task '{name}' not found")

    def tasks(self) -> List[Task]:
        return self._tasks
