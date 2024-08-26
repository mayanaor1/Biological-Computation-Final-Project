# Biological-Computation-Final-Project


This Python program identifies monotonic functions based on a set of configurations and displays the results using a graphical table. Monotonic functions are those where the output does not decrease as the inputs increase, based on a specific set of criteria.

## Overview

The program evaluates all possible binary functions for a given set of configurations and determines which ones meet the monotonicity requirement. A function is considered monotonic if its output values do not decrease as the input values increase according to the specified conditions.

### How It Works

1. **Generate Functions:**
   - The program generates all possible functions using binary representations. Each function corresponds to a unique combination of binary values for all configurations.

2. **Monotonicity Check:**
   - The program evaluates whether each function meets the monotonicity condition. This involves checking if, as the configuration values increase, the function values either stay the same or increase.

3. **Filter and Display:**
   - Functions that satisfy the monotonicity condition are collected and displayed both in the console and in a graphical user interface (GUI) created with Tkinter.

## Requirements

Ensure you have Python 3.x installed. You will also need the following libraries:

- `pandas` for data manipulation.
- `tabulate` for tabular data formatting.
- `termcolor` for colored terminal output.
- `tkinter` for GUI elements (usually included with Python).



## Output

When you run the program, the output is presented in two main parts: the console output and the Tkinter GUI.

### Console Output

The console will display information about the number of monotonic functions and their binary representations. For example:


```plaintext
Number of monotonic functions: 3
Monotonic Function 1: [0, 1, 1, 0, 1, 1, 0, 1, 1]
Monotonic Function 2: [1, 1, 0, 1, 1, 1, 0, 1, 0]
Monotonic Function 3: [0, 0, 1, 0, 1, 1, 1, 1, 1]
```

### Tkinter GUI

The Tkinter GUI will open and display a table where each row represents a monotonic function. The columns include the function label and the values for each configuration.

Example table layout:

| Function             | (0,0,0,0) | (1,0,0,0) | (1,1,0,0) | (0,0,1,0) | (1,0,1,0) | (1,1,1,0) | (0,0,1,1) | (1,0,1,1) | (1,1,1,1) |
|----------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| Monotonic Function 1 | 0         | 1         | 1         | 0         | 1         | 1         | 0         | 1         | 1         |
| Monotonic Function 2 | 1         | 1         | 0         | 1         | 1         | 1         | 0         | 1         | 0         |
| Monotonic Function 3 | 0         | 0         | 1         | 0         | 1         | 1         | 1         | 1         | 1         |

Each row corresponds to a different monotonic function with its binary values for each configuration.



