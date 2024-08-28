# Biological-Computation-Final-Project


This Python program identifies monotonic functions based on a set of configurations and displays the results using a graphical table. Monotonic functions are those where the output does not decrease as the inputs increase, based on a specific set of criteria.

## How It Works

### 1. Definitions and Configurations

- **Configurations**: The program defines a list of binary configurations, each represented as a tuple of 0s and 1s, covering all relevant input scenarios. Since each quartet includes two activators and two inhibitors, not all possible combinations are considered. For example, a scenario where only the first activator is active is treated the same as a scenario where only the second activator is active.


- **Functions**: It generates all possible Boolean functions that can be applied to these configurations. Each function is represented as a list of 0s and 1s.

### 2. Monotonicity Check

The program checks whether each generated Boolean function is monotonic. A function is considered monotonic if its output does not decrease when the input configuration increases.

- Two key functions are used:
  - `is_monotonic(function)`: Checks if the function is monotonic by comparing outputs for different configurations.
  - `compare_configs(config1, config2, value1, value2)`: Compares two configurations and their function outputs to determine monotonicity.

- Check boundary conditions:
   - The value for the configuration (1,1,0,0) should be 1.
   - The value for the configuration (1,1,1,1) should be 0.
 
### 3. Filtering

- After generating all possible functions, the program filters out non-monotonic functions, leaving only the monotonic ones.

### 4. Output

- The program prints the number and details of the monotonic functions.

- It prepares a table where each row represents a monotonic function, showing its output for each configuration.

### 5. Jupyter Notebook Display

The program uses pandas to create a DataFrame and displays it with custom styling in a Jupyter Notebook.

Cell colors are customized:

- Cells with a value of 1 are colored red.
- Cells with a value of 0 are colored white.
  
### 6. Execution

- The program runs a Tkinter event loop to keep the GUI open, allowing users to view the table of monotonic functions.

## Requirements

Ensure you have Python 3.x installed. You will also need the following libraries:

- pandas for data manipulation.
- jinja2 for rendering styled DataFrames in Jupyter Notebook.


## Output

The console will display information about the number of monotonic functions and their binary representations:


```plaintext
Number of monotonic functions: 18
Monotonic Function 1: [0, 0, 1, 0, 0, 0, 0, 0, 0]
Monotonic Function 2: [0, 0, 1, 0, 0, 1, 0, 0, 0]
Monotonic Function 3: [0, 0, 1, 0, 0, 1, 0, 0, 1]
Monotonic Function 4: [0, 1, 1, 0, 0, 0, 0, 0, 0]
Monotonic Function 5: [0, 1, 1, 0, 0, 1, 0, 0, 0]
Monotonic Function 6: [0, 1, 1, 0, 0, 1, 0, 0, 1]
Monotonic Function 7: [0, 1, 1, 0, 1, 1, 0, 0, 0]
Monotonic Function 8: [0, 1, 1, 0, 1, 1, 0, 0, 1]
Monotonic Function 9: [0, 1, 1, 0, 1, 1, 0, 1, 1]
Monotonic Function 10: [1, 1, 1, 0, 0, 0, 0, 0, 0]
Monotonic Function 11: [1, 1, 1, 0, 0, 1, 0, 0, 0]
Monotonic Function 12: [1, 1, 1, 0, 0, 1, 0, 0, 1]
Monotonic Function 13: [1, 1, 1, 0, 1, 1, 0, 0, 0]
Monotonic Function 14: [1, 1, 1, 0, 1, 1, 0, 0, 1]
Monotonic Function 15: [1, 1, 1, 0, 1, 1, 0, 1, 1]
Monotonic Function 16: [1, 1, 1, 1, 1, 1, 0, 0, 0]
Monotonic Function 17: [1, 1, 1, 1, 1, 1, 0, 0, 1]
Monotonic Function 18: [1, 1, 1, 1, 1, 1, 0, 1, 1]



```


the program is also outputs a styled DataFrame with the following features:

- Red Cells: Cells containing the value 1.
- White Cells: Cells containing the value 0.
- Yellow Borders: Continuous borders around the columns (1, 1, 0, 0) and (0, 0, 1, 1).

| Function   | (0,0,0,0) | (1,0,0,0) | (1,1,0,0) | (0,0,1,0) | (1,0,1,0) | (1,1,1,0) | (0,0,1,1) | (1,0,1,1) | (1,1,1,1) |
|------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| Function 1 | 0         | 0         | 1         | 0         | 0         | 0         | 0         | 0         | 0         |
| Function 2 | 0         | 0         | 1         | 0         | 0         | 1         | 0         | 0         | 0         |
| Function 3 | 0         | 0         | 1         | 0         | 0         | 1         | 0         | 0         | 1         |
| Function 4 | 0         | 1         | 1         | 0         | 0         | 0         | 0         | 0         | 0         |
| Function 5 | 0         | 1         | 1         | 0         | 0         | 1         | 0         | 0         | 0         |
| Function 6 | 0         | 1         | 1         | 0         | 0         | 1         | 0         | 0         | 1         |
| Function 7 | 0         | 1         | 1         | 0         | 1         | 1         | 0         | 0         | 0         |
| Function 8 | 0         | 1         | 1         | 0         | 1         | 1         | 0         | 0         | 1         |
| Function 9 | 0         | 1         | 1         | 1         | 1         | 1         | 0         | 1         | 1         |
| Function 10| 1         | 1         | 1         | 0         | 0         | 0         | 0         | 0         | 0         |
| Function 11| 1         | 1         | 1         | 0         | 0         | 1         | 0         | 0         | 0         |
| Function 12| 1         | 1         | 1         | 0         | 0         | 1         | 0         | 0         | 1         |
| Function 13| 1         | 1         | 1         | 0         | 1         | 1         | 0         | 0         | 0         |
| Function 14| 1         | 1         | 1         | 0         | 1         | 1         | 0         | 0         | 1         |
| Function 15| 1         | 1         | 1         | 0         | 1         | 1         | 0         | 1         | 1         |
| Function 16| 1         | 1         | 1         | 1         | 1         | 1         | 0         | 0         | 0         |
| Function 17| 1         | 1         | 1         | 1         | 1         | 1         | 0         | 0         | 1         |
| Function 18| 1         | 1         | 1         | 1         | 1         | 1         | 0         | 1         | 1         |


Each row corresponds to a different monotonic function with its binary values for each configuration.



