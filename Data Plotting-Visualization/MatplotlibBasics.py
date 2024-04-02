"""
Script By Nebulight
nebulight.info.gf
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_function(x, y, title):
    """
    Plots a function.

    Args:
    x (array-like): Input values for the function.
    y (array-like): Output values of the function.
    title (str): Title for the plot.
    """
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

def animate_function(x, y, title):
    """
    Animates a function.

    Args:
    x (array-like): Input values for the function.
    y (array-like): Output values of the function.
    title (str): Title for the animation.
    """
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))
    ax.set_title(title)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.grid(True)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        line.set_data(x[:i], y[:i])
        return line,

    ani = animation.FuncAnimation(fig, animate, frames=len(x), init_func=init, blit=True)
    plt.show()

if __name__ == "__main__":
    mode = input("Enter 'animated' or 'non-animated' to choose the mode: ").lower()
    function = input("Enter the function you want to plot (e.g., 'sin', 'cos'): ").lower()
    start = float(input("Enter the start value for x: "))
    end = float(input("Enter the end value for x: "))
    step = float(input("Enter the step size for x: "))

    x = np.arange(start, end, step)
    if function == 'sin':
        y = np.sin(x)
        title = "Plot of Sin(x)"
    elif function == 'cos':
        y = np.cos(x)
        title = "Plot of Cos(x)"
    else:
        raise ValueError("Invalid function. Please choose 'sin' or 'cos'.")

    if mode == 'animated':
        animate_function(x, y, title)
    elif mode == 'non-animated':
        plot_function(x, y, title)
    else:
        raise ValueError("Invalid mode. Please choose 'animated' or 'non-animated'.")
