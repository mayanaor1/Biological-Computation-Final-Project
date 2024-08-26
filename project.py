import tkinter as tk
from tkinter import ttk
from itertools import product
import pandas as pd
from tabulate import tabulate
from termcolor import colored


def is_monotonic(function):
    """
    Check if a given function is monotonic.

    A function is considered monotonic if, for every pair of configurations,
    the function's value does not decrease as the configuration values increase.
    """
    # Check boundary conditions:
    # - The value for the configuration (1,1,0,0) should be 1.
    # - The value for the configuration (1,1,1,1) should be 0.
    if function[2] != 1 or function[6] != 0:
        return False

    # Use zip to iterate over pairs of configurations and function values
    for (config1, value1), (config2, value2) in product(zip(configurations, function), repeat=2):
        if not compare_configs(config1, config2, value1, value2):
            return False

    return True


def compare_configs(config1, config2, value1, value2):
    """
    Compare two configurations and their associated function values.

    The function is considered monotonic if:
    - config1 is less than or equal to config2 in all dimensions
    - value1 is less than or equal to value2
    """
    # Compare configurations based on their components
    if (config1[0] <= config2[0] and config1[1] <= config2[1] and
            config1[2] >= config2[2] and config1[3] >= config2[3]):
        return value1 <= value2
    return True


# List of possible configurations
configurations = [
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 0, 1, 0),
    (1, 0, 1, 0),
    (1, 1, 1, 0),
    (0, 0, 1, 1),
    (1, 0, 1, 1),
    (1, 1, 1, 1),
]

# Generate all possible functions for the given configurations
functions = []
num_conf = len(configurations)
num_functions = 2 ** num_conf
for i in range(num_functions):
    function = []
    for j in range(num_conf):
        function.append((i >> j) & 1)
    functions.append(function)

# Filter functions that are monotonic
monotonic_functions = [f for f in functions if is_monotonic(f)]

# Print the number of monotonic functions
print(f"Number of monotonic functions: {len(monotonic_functions)}")

# Print the list of monotonic functions
for idx, function in enumerate(monotonic_functions, start=1):
    print(f"Monotonic Function {idx}: {function}")

# Prepare data for displaying in a table
headers = ["Function"] + [str(conf) for conf in configurations]
data = []
for i, function in enumerate(monotonic_functions):
    row = [f"Function {i + 1}"]  # Start the row with the function label
    row.extend(function)  # Add the function values for all scenarios
    data.append(row)

# Create a DataFrame for displaying in the Tkinter GUI
df = pd.DataFrame(data, columns=headers)

# Create the main Tkinter window
root = tk.Tk()
root.title("Monotonic Functions")

# Create a Treeview widget for displaying the data
tree = ttk.Treeview(root, columns=headers, show="headings")
tree.pack(expand=True, fill="both")

# Define column headers and set their width
for header in headers:
    tree.heading(header, text=header)
    tree.column(header, width=100)

# Add rows to the Treeview widget
for row in data:
    tree.insert("", "end", values=row)

# Start the Tkinter event loop
root.mainloop()
