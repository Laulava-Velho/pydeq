from .plotting import plot_streamplot, plot_directionfield, plot_vectorfield, plot_zeros
from typing import Callable
from .types import Data
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib

# Set the TeX system to to the available one
matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'

def get_worker(task_name: str) -> Callable[[Axes, Data], None]:
    if task_name == "streamplot":
        return plot_streamplot
    elif task_name == "directionfield":
        return plot_directionfield
    elif task_name == "vectorfield":
        return plot_vectorfield
    elif task_name == "zeros":
        return plot_zeros
    else:
        raise ValueError(f"Unknown task name: {task_name}")

def run(ax: Axes, data: Data):

    tasks = data.tasks()

    for task in tasks:
        worker = get_worker(task.name)
        worker(ax, data)

def save_plot(fig: Figure):
    print("Do you want to save the plot? [yes|no]")
    answer = input().lower()
    if answer == "yes":
        print("Enter the file name:")
        filename = input()
        fig.savefig(filename)
    else:
        print("Okay, plot not saved.")
