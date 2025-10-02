import sys
import argparse
import importlib.util
import matplotlib.pyplot as plt
from src.run_utils import run, save_plot

def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None:
        raise ValueError(f"Failed to create spec for {file_path}")
    else:
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        loader = spec.loader
        if loader is None:
            raise ValueError(f"Failed to create loader for {file_path}")
        else:
            loader.exec_module(module)
            return module

def load(sem_tag: str = '1'):
    module = import_from_path(f"sem{sem_tag}", f"./examples/sem{sem_tag}.py")
    return module

def format_args(args):
    if args.ex is None:
        args.ex = []
    args.ex = [int(entry) for entry in args.ex]
    return args

def parse_args():
    parser = argparse.ArgumentParser(description='Run the program')
    parser.add_argument('--sem', type=str, default=1, help='Which seminar to load. Default is 1.')
    parser.add_argument('--ex', type=int, nargs='*', help='Which examples to load. By default, all examples are loaded.')
    parser.add_argument('--save', action='store_true', help='Save the plot to a file.')
    args = parser.parse_args()
    args = format_args(args)
    return args

if __name__ == "__main__":

    args = parse_args()
    ex_list = load(sem_tag = args.sem).ex_list
    if args.ex:
        ex_list = [ex_list[i - 1] for i in args.ex if 1 <= i <= len(ex_list)]

    for data in ex_list:
        fig, ax = plt.subplots(figsize=(16 , 12))
        ax.grid()
        run(ax, data)
        ax.set_aspect('equal')
        ax.set_xlabel(data.x_label)
        ax.set_ylabel(data.y_label)
        plt.show()
        if args.save:
            save_plot(fig)

    print("Thank you for using the program.")
