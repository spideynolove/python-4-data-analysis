# QA list

# Table of Contents

- [QA list](#qa-list)
- [Table of Contents](#table-of-contents)
  - [What are element-wise computations?](#what-are-element-wise-computations)
    - [NumPy Arrays](#numpy-arrays)
    - [Pandas Series and DataFrames](#pandas-series-and-dataframes)
    - [Element-Wise Functions](#element-wise-functions)
    - [Benefits of Element-Wise Computations](#benefits-of-element-wise-computations)
  - [What is linear algebra?](#what-is-linear-algebra)
  - [lists all Linear algebra operations of numpy](#lists-all-linear-algebra-operations-of-numpy)
  - [What pandas features are equivalent to using SQL?](#what-pandas-features-are-equivalent-to-using-sql)
  - [Explain and show how to use reshape, slice and dice, aggregations, select subsets of data functions in pandas](#explain-and-show-how-to-use-reshape-slice-and-dice-aggregations-select-subsets-of-data-functions-in-pandas)
    - [Reshape:](#reshape)
    - [Slice and Dice:](#slice-and-dice)
    - [Aggregations:](#aggregations)
    - [Select Subsets of Data:](#select-subsets-of-data)
  - [In python, Everything is an object](#in-python-everything-is-an-object)
  - [What is Dynamic references, strong types](#what-is-dynamic-references-strong-types)
  - [Python objects attributes and methods](#python-objects-attributes-and-methods)
    - [Object Attributes:](#object-attributes)
    - [Object Methods:](#object-methods)

## What are element-wise computations?

Element-wise computations refer to operations performed independently on **each element of a data structure**, such as **arrays, matrices, or vectors**. In Python, libraries like NumPy and Pandas provide powerful tools for performing these element-wise operations efficiently.

### NumPy Arrays
In NumPy, element-wise operations are a fundamental concept. When you perform an operation on two NumPy arrays, the operation is applied element-wise. For example:

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise addition
result_addition = arr1 + arr2  # [5, 7, 9]

# Element-wise multiplication
result_multiply = arr1 * arr2  # [4, 10, 18]
```

### Pandas Series and DataFrames
In Pandas, element-wise computations also apply to Series and DataFrames. Operations between Series or DataFrames are also performed element-wise:

```python
import pandas as pd

# Creating two Pandas Series
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

# Element-wise addition of Series
result_addition = s1 + s2  # [5, 7, 9]

# Creating a Pandas DataFrame
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# Element-wise addition of DataFrames
result_addition_df = df1 + df2
# Result:
#     A   B
# 0   8  14
# 1  10  16
# 2  12  18
```

### Element-Wise Functions
In addition to basic arithmetic operations, many functions in Python libraries like NumPy and Pandas are also designed to be applied element-wise. For example:

```python
import numpy as np

arr = np.array([1, 2, 3])

# Element-wise square root
result_sqrt = np.sqrt(arr)  # [1.        1.41421356 1.73205081]

# Element-wise exponentiation
result_exp = np.exp(arr)  # [ 2.71828183  7.3890561  20.08553692]
```

### Benefits of Element-Wise Computations
- **Efficiency**: Element-wise computations are typically optimized in libraries like NumPy and Pandas, making them efficient for large datasets.
  
- **Simplicity**: When working with arrays or matrices, element-wise operations provide a simple and intuitive way to apply operations to every element.

- **Broadcasting**: In NumPy, broadcasting allows element-wise operations between arrays of different shapes. Broadcasting rules automatically expand dimensions of arrays to make computations possible.


## What is linear algebra?

Linear algebra is like a special set of rules we use to work with shapes and patterns, kind of like when we play with building blocks or puzzle pieces. It helps us solve problems by looking at how things change and move around.

We use linear algebra to:
- Draw lines and shapes on a computer screen.
- Make computer games and animations.
- Understand how things move and change in the world, like when we want to know where a car will be after driving for an hour.
- Help scientists and engineers design new things, like buildings, bridges, and even medicines.

## lists all Linear algebra operations of numpy

NumPy is a powerful library for numerical computing in Python, and it provides a wide range of linear algebra operations. NumPy's linear algebra module (`np.linalg`).

1. **Matrix Multiplication / Dot Product**:
   - `np.dot(a, b)`: Computes the dot product of two arrays. For 2-D arrays, it is equivalent to matrix multiplication.

2. **Element-wise Multiplication**:
   - `np.multiply(a, b)`: Element-wise multiplication of two arrays.
   - `a * b`: The `*` operator also performs element-wise multiplication.

3. **Matrix Transpose**:
   - `np.transpose(a)`: Transposes the array. For 2-D arrays, it flips the rows and columns.

4. **Matrix Inverse**:
   - `np.linalg.inv(a)`: Computes the multiplicative inverse of a matrix.

5. **Matrix Determinant**:
   - `np.linalg.det(a)`: Computes the determinant of a square matrix.

6. **Eigenvalues and Eigenvectors**:
   - `np.linalg.eig(a)`: Computes the eigenvalues and eigenvectors of a square matrix.
   - `np.linalg.eigh(a)`: Computes the eigenvalues and eigenvectors of a symmetric or Hermitian matrix.
   - `np.linalg.eigvals(a)`: Computes the eigenvalues of a square matrix.

7. **Solving Linear Equations**:
   - `np.linalg.solve(a, b)`: Solves a linear matrix equation, `ax = b`, for `x`.

8. **Singular Value Decomposition (SVD)**:
   - `np.linalg.svd(a)`: Computes the singular value decomposition of a matrix.

9. **QR Decomposition**:
   - `np.linalg.qr(a)`: Computes the QR decomposition of a matrix.

10. **Cholesky Decomposition**:
    - `np.linalg.cholesky(a)`: Computes the Cholesky decomposition of a matrix.

11. **Matrix Rank**:
    - `np.linalg.matrix_rank(a)`: Computes the rank of a matrix.

12. **Pseudo-inverse**:
    - `np.linalg.pinv(a)`: Computes the Moore-Penrose pseudo-inverse of a matrix.

13. **Norms**:
    - `np.linalg.norm(a)`: Computes the norm of a vector or matrix.
    - `np.linalg.norm(a, ord=1)`: Computes the L1 norm (sum of absolute values).
    - `np.linalg.norm(a, ord=2)`: Computes the L2 norm (Euclidean norm).
    - `np.linalg.norm(a, ord=np.inf)`: Computes the L-infinity norm (maximum absolute row sum).

## What pandas features are equivalent to using SQL?

1. **Selecting Columns**:
   - Pandas: `df['column_name']` or `df.column_name`
   - SQL: `SELECT column_name FROM table_name`

2. **Filtering Rows**:
   - Pandas: `df[df['column_name'] > value]`
   - SQL: `SELECT * FROM table_name WHERE column_name > value`

3. **Grouping and Aggregating**:
   - Pandas: `df.groupby('column_name').agg({'column_name': 'function'})`
   - SQL: `SELECT column_name, function(column_name) FROM table_name GROUP BY column_name`

4. **Sorting**:
   - Pandas: `df.sort_values('column_name')`
   - SQL: `SELECT * FROM table_name ORDER BY column_name`

5. **Joining Tables**:
   - Pandas: `pd.merge(df1, df2, on='column_name', how='inner')`
   - SQL: `SELECT * FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name`

6. **Adding New Columns**:
   - Pandas: `df['new_column'] = ...`
   - SQL: `ALTER TABLE table_name ADD new_column ...`

7. **Removing Columns**:
   - Pandas: `df.drop(columns=['column_name'])`
   - SQL: `ALTER TABLE table_name DROP COLUMN column_name`

8. **Counting Rows**:
   - Pandas: `df['column_name'].count()`
   - SQL: `SELECT COUNT(column_name) FROM table_name`

9. **Unique Values**:
   - Pandas: `df['column_name'].unique()`
   - SQL: `SELECT DISTINCT column_name FROM table_name`

## Explain and show how to use reshape, slice and dice, aggregations, select subsets of data functions in pandas

### Reshape:
- **Explanation**: Reshaping is like changing the shape of a table. It's like taking LEGO pieces and building different shapes.
- **Example**:
  ```python
  import pandas as pd

  # Create a DataFrame
  data = {
      'A': [1, 2, 3],
      'B': [4, 5, 6],
      'C': [7, 8, 9]
  }
  df = pd.DataFrame(data)

  # Reshape to a different shape
  reshaped_df = df.values.reshape(3, 3)

  # Display the reshaped DataFrame
  print(reshaped_df)
  ```

### Slice and Dice:
- **Explanation**: Slicing is like cutting out pieces of a pizza. We can get just the parts we want from our table.
- **Example**:
  ```python
  # Slice and dice the DataFrame
  sliced_df = df.iloc[1:, 1:3]  # Selects rows 1 and 2, columns 1 and 2

  # Display the sliced DataFrame
  print(sliced_df)
  ```

### Aggregations:
- **Explanation**: Aggregations are like counting how many LEGO pieces we have or finding the average size. It helps us summarize our data.
- **Example**:
  ```python
  # Aggregation example
  sum_column = df['A'].sum()  # Adds up all values in column 'A'
  average_column = df['B'].mean()  # Calculates the average of values in column 'B'

  # Display the results
  print("Sum of column 'A':", sum_column)
  print("Average of column 'B':", average_column)
  ```

### Select Subsets of Data:
- **Explanation**: Selecting subsets is like picking out certain LEGO pieces we want to play with. It helps us focus on specific parts of our data.
- **Example**:
  ```python
  # Select subset based on condition
  subset_df = df[df['A'] > 1]  # Selects rows where 'A' is greater than 1

  # Display the subset DataFrame
  print(subset_df)
  ```

## In python, Everything is an object

Imagine Python as a big LEGO set where everything you work with, like numbers, words, or even a whole game you're making, is a special LEGO piece. Each piece has its own unique abilities and things it can do.

Now, when we say "Everything is an object in Python," it's like saying everything we work with in Python is a special LEGO piece. Just like how every LEGO piece has its own shape, color, and what it can do (like a wheel can roll, and a brick can stack), in Python, every piece of data is like a special LEGO object with its own set of rules and things it can do.

So, whether it's a number, a word, a list of things, or even a whole program you write, they are all like special LEGO pieces (objects) in Python. And just like you can build awesome things with LEGO pieces, in Python, we can do cool and powerful things with these objects!

## What is Dynamic references, strong types

Imagine Python as a game where you can change the rules as you play, and each player (or object) follows those rules really well.

1. **Dynamic References**:
   - It's like giving nicknames to your friends based on what they're doing at the moment.
   - In Python, you can change what a name (variable) points to whenever you want.
   - Example:
     ```python
     x = 5  # x is the nickname for the number 5
     x = "hello"  # Now, x is the nickname for the word "hello"
     ```

2. **Strong Types**:
   - It's like knowing exactly what kind of LEGO piece you have, even if you change its name.
   - In Python, each object has a specific type (like number, word, list), and Python always keeps track of this.
   - Example:
     ```python
     x = 5  # x is a number
     y = "hello"  # y is a word
     z = x + y  # This would give an error because we can't add a number and a word
     ```

## Python objects attributes and methods

In Python, objects are like special LEGO pieces with their own abilities and things they can do. Just like a LEGO piece can have different colors and functions, objects in Python have attributes (characteristics) and methods (things they can do).

### Object Attributes:
- **Explanation**: Attributes are like the special features of a LEGO piece. They describe what the object is like.
- **Example**:
  ```python
  # Example with a car object
  class Car:
      def __init__(self, color, brand):
          self.color = color  # Attribute: color
          self.brand = brand  # Attribute: brand

  # Create a car object
  my_car = Car("red", "Toyota")

  # Access and use the attributes
  print("My car is a", my_car.color, my_car.brand)
  ```

### Object Methods:
- **Explanation**: Methods are like the actions a LEGO piece can perform. They are things the object can do.
- **Example**:
  ```python
  # Example with a dog object
  class Dog:
      def __init__(self, name):
          self.name = name

      def bark(self):
          print(self.name, "says Woof!")

  # Create a dog object
  my_dog = Dog("Buddy")

  # Use the method to make the dog bark
  my_dog.bark()  # This will print: Buddy says Woof!
  ```
- getattr function
