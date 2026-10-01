# 🔢 NumPy Analyzer

> A menu-driven Python application built with **NumPy** and **Object-Oriented Programming (OOP)** to create, manipulate, search, sort, filter, and analyze 1D, 2D, and 3D arrays.

---

## 📌 Project Overview

**NumPy Analyzer** is a command-line project that helps users practice NumPy array operations through an interactive menu. Users can create arrays by entering dimensions and values, then perform indexing, slicing, arithmetic, combining, splitting, searching, sorting, filtering, and statistical calculations.

The project also demonstrates OOP concepts through a `DataAnalytics` class that stores the current array in a private attribute.

## ✨ Features

- 🧱 **Create arrays:** Create 1D, 2D, and 3D arrays using user input.
- 🎯 **Indexing:** Access elements by index, row and column, or depth, row and column.
- ✂️ **Slicing:** Extract selected portions of 1D, 2D, and 3D arrays.
- ➕ **Mathematical operations:** Perform element-wise addition, subtraction, multiplication, and division.
- 🔗 **Combine arrays:** Use NumPy's `hstack()` and `vstack()`.
- 🧩 **Split arrays:** Use `hsplit()` and `vsplit()`.
- 🔍 **Search:** Locate matching values using `np.where()`.
- 🔃 **Sort:** Sort values in ascending or descending order.
- 🎚️ **Filter:** Select even numbers, odd numbers, values greater than a chosen number, or values less than a chosen number.
- 📊 **Statistics:** Calculate sum, mean, median, standard deviation, variance, minimum, and maximum.

## 🖥️ Main Menu

```text
1. Create a NumPy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
```

## 🏗️ OOP Concepts Used

### Class and Object

The `DataAnalytics` class groups the array-related functionality. An object is created with:

```python
n1 = DataAnalytics()
```

### Constructor

```python
def __init__(self, number=None):
    self.__number = number
```

The constructor initializes the object's array value.

### Encapsulation and Private Attribute

`self.__number` is a name-mangled attribute used to keep the current array inside the class. The `get_array()` method provides access to the stored array:

```python
def get_array(self):
    return self.__number
```

### Instance Methods

- `create_1d()` — creates and stores a 1D array.
- `create_2d()` — creates and stores a 2D array.
- `create_3d()` — creates and stores a 3D array.
- `get_array()` — returns the currently stored array.

## 🧮 NumPy Operations

| Operation | Example | Purpose |
|---|---|---|
| Array creation | `np.array()` | Creates an array |
| Reshape | `arr.reshape(rows, columns)` | Changes the array shape |
| Dimensions | `arr.ndim` | Returns the number of dimensions |
| Horizontal stack | `np.hstack((arr1, arr2))` | Combines arrays horizontally |
| Vertical stack | `np.vstack((arr1, arr2))` | Combines arrays vertically |
| Horizontal split | `np.hsplit(arr, parts)` | Splits an array horizontally |
| Vertical split | `np.vsplit(arr, parts)` | Splits an array vertically |
| Search | `np.where(arr == value)` | Finds indices matching a condition |
| Sorting | `np.sort(arr)` | Sorts array values |
| Filtering | `arr[arr > value]` | Selects values matching a condition |
| Sum | `np.sum(arr)` | Calculates the total |
| Mean | `np.mean(arr)` | Calculates the average |
| Median | `np.median(arr)` | Finds the median |
| Standard deviation | `np.std(arr)` | Measures spread around the mean |
| Variance | `np.var(arr)` | Measures squared spread |
| Minimum / Maximum | `np.min(arr)`, `np.max(arr)` | Finds the smallest/largest value |

## 🧪 Example: Creating a 3D Array

For 2 layers, 2 rows, and 3 columns, enter 12 numbers:

```text
Layer: 2
Rows: 2
Columns: 3
Elements: 1 2 3 4 5 6 7 8 9 10 11 12
```

Output:

```text
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
```

The array is reshaped using:

```python
arr3d = arr.reshape(layer, rows, columns)
```

## 🛠️ Technologies Used

- 🐍 **Python**
- 🔢 **NumPy**
- 🏗️ **Object-Oriented Programming**
- 💻 **Command-line interface**

## 📂 Project Structure

```text
NumPy-Analyzer/
├── p8.py
└── README.md
```

- `p8.py` — main application.
- `README.md` — project documentation.

> If your Python file has a different name, replace `p8.py` in the commands below with your filename.

## ⚙️ Installation and Setup

### 1. Check Python

```bash
python --version
```

### 2. Install NumPy

```bash
pip install numpy
```

### 3. Run the Application

```bash
python p8.py
```

## 📚 Learning Outcomes

By building this project, you can practice:

- Creating and reshaping multidimensional NumPy arrays.
- Understanding dimensions and indexing in 1D, 2D, and 3D arrays.
- Using slicing to select parts of arrays.
- Performing element-wise arithmetic.
- Combining and splitting arrays.
- Searching, sorting, and filtering numerical data.
- Calculating common statistical measures.
- Organizing functionality with classes, objects, constructors, instance methods, and encapsulation.
- Building an interactive menu using Python's `while` loop and `match-case`.

## 🚀 Possible Future Improvements

- 🛡️ Add input validation and exception handling.
- 📏 Validate that the number of entered elements matches the requested dimensions.
- ⚖️ Check that arrays have compatible shapes before arithmetic or stacking.
- ➗ Handle division by zero.
- 📁 Add CSV import and export.
- 📈 Add visualizations using Matplotlib.
- 🧹 Separate menu handling from array operations for cleaner OOP design.

## 👨‍💻 Author

**Sanjay Kushwaha**  
🐍 Python Learner | 📊 Data Analysis Enthusiast

## 📜 License

Created for educational and learning purposes. You may adapt and improve it for your own practice.
