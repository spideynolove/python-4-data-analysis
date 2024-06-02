# Python for Data Analysis - Wes McKinney

# Table of Contents

- [Python for Data Analysis - Wes McKinney](#python-for-data-analysis---wes-mckinney)
- [Table of Contents](#table-of-contents)
  - [About the Book](#about-the-book)
  - [Key Features](#key-features)
  - [Installation](#installation)
  - [Using This Repository](#using-this-repository)
  - [Resources](#resources)
  - [Preliminaries](#preliminaries)
  - [Python Language Basics, IPython, and Jupyter Notebooks](#python-language-basics-ipython-and-jupyter-notebooks)
  - [Built-In Data Structures, Functions, and Files](#built-in-data-structures-functions-and-files)
  - [NumPy Basics: Arrays and Vectorized Computation](#numpy-basics-arrays-and-vectorized-computation)
  - [Getting Started with pandas](#getting-started-with-pandas)
  - [Data Loading, Storage, and File Formats](#data-loading-storage-and-file-formats)
  - [Data Cleaning and Preparation](#data-cleaning-and-preparation)
  - [Data Wrangling: Join, Combine, and Reshape](#data-wrangling-join-combine-and-reshape)
  - [Plotting and Visualization](#plotting-and-visualization)
  - [Data Aggregation and Group Operations](#data-aggregation-and-group-operations)
  - [Time Series](#time-series)
  - [Advanced pandas](#advanced-pandas)
  - [Advanced NumPy](#advanced-numpy)

## About the Book
"Python for Data Analysis" is authored by Wes McKinney, the creator of the pandas library. This book serves as a comprehensive guide to manipulating, processing, cleaning, and crunching datasets in Python. Updated to include Python 3.10 and pandas 1.4, it's ideal for both beginners and experienced users who want to deepen their understanding of data analysis tools in Python.

## Key Features
- **Hands-on with pandas and NumPy**: Learn how to use pandas for data manipulation and NumPy for numerical computation.
- **Data Wrangling**: Dive deep into practical techniques to handle and prepare data for analysis.
- **Visualization**: Use matplotlib to create informative visualizations.
- **Efficient Data Analysis**: Apply efficient data analysis techniques to process large datasets.
- **Real-world Examples**: Each chapter includes examples and case studies that demonstrate how to apply Python tools to solve data analysis problems.

## Installation
Instructions for setting up Python and the necessary libraries are detailed in the book and can be found in the official documentation.

## Using This Repository
- **Examples**: The `examples/` directory contains Jupyter notebooks that replicate the book's examples.
- **Datasets**: The `datasets/` folder hosts the data used in examples and exercises throughout the book.
- **Exercises**: Practice exercises and solutions to solidify your understanding and application of Python data tools.

## Resources
- [Official pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [NumPy User Guide](https://numpy.org/doc/stable/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

---
## Preliminaries
- **Purpose and Focus**: Introduces the book’s aim to teach data manipulation using Python, emphasizing pandas, NumPy, and IPython.
- **Python for Data Analysis**: Discusses Python’s suitability for data analysis, highlighting its role as a glue language and the benefits of its scientific libraries.
- **Essential Python Libraries**: Reviews NumPy for numerical operations, pandas for data handling, matplotlib for plotting, and other key libraries.
   - **NumPy**: For numerical operations and array manipulation.
   - **pandas**: For data manipulation and analysis.
   - **matplotlib**: For data visualization.
   - **IPython and Jupyter**: For interactive computing and notebooks.
   - **SciPy**: For scientific and technical computing.
   - **scikit-learn**: For machine learning.
   - **statsmodels**: For statistical modeling.
- **Installation and Setup**: Provides detailed guidance for setting up Python and necessary libraries using Miniconda and conda-forge.
- **Navigating the Book**: Outlines how to approach the book based on readers’ familiarity with Python, detailing the structure and flow of content.
- **Community and Conferences**: Encourages engagement with the Python data science community and participation in relevant conferences.

## Python Language Basics, IPython, and Jupyter Notebooks
- **Python Interpreter**: Discusses the use of Python as an interpreted language and introduces the interactive Python interpreter.
  - Introduction to Python's interactive mode (REPL) and script mode.
  - Instructions on how to start the Python interpreter in different environments.
- **IPython Basics**: Describes the advanced features of IPython, including tab completion, object introspection, and embedded shell commands.
  - **Running the IPython Shell**: Enhanced interactive Python shell with features like tab completion, history, and magic commands.
  - **Running the Jupyter Notebook**: Interactive web-based environment for writing and running code.
  - **Tab Completion**: Helps to complete variable names, functions, and file paths.
  - **Introspection**: Using `?` and `??` to get information about objects, including documentation and source code.
- **Jupyter Notebooks**: Explains how to use Jupyter Notebooks for combining executable code, rich text, and graphics in a web-based interface.
- **Python Language Basics**: Covers Python syntax, built-in data structures like lists, dictionaries, sets, tuples, functions, and file operations.
  - **Language Semantics**:
    - **Indentation**: Python uses indentation to define blocks of code.
    - **Comments**: Lines starting with `#` are comments and not executed.
    - **Function and Object Calls**: How to call functions and use objects.
  - **Scalar Types**:
    - **Numbers**: Integers, floats, and complex numbers.
    - **Strings**: Text data type, creating and manipulating strings.
    - **Booleans**: True and False values, often used in control flow statements.
    - **None**: Represents the absence of a value.
  - **Control Flow**:
    - **if, elif, else**: Conditional statements.
    - **for loops**: Iterating over sequences like lists or ranges.
    - **while loops**: Repeating code while a condition is true.
    - **pass**: A null operation; a placeholder for future code.
    - **range**: Generating sequences of numbers for iteration.

## Built-In Data Structures, Functions, and Files
- **Data Structures and Sequences**: Details the use of tuples, lists, dictionaries, and sets, including comprehensive examples and special methods.
  - **Tuple**:
    - Immutable, fixed-length sequence of Python objects.
    - Created with parentheses or `tuple()` function.
    - Elements accessed using square brackets.

  - **List**:
    - Mutable, variable-length sequence.
    - Created with square brackets or `list()` function.
    - Supports indexing, slicing, and methods like `append()`, `remove()`, etc.

  - **Dictionary**:
    - Collection of key-value pairs.
    - Created with curly braces `{}` or `dict()` function.
    - Keys are unique and used to access corresponding values.

  - **Set**:
    - Unordered collection of unique elements.
    - Created with curly braces `{}` or `set()` function.
    - Supports operations like union, intersection, and difference.

  - **Built-In Sequence Functions**:
    - Functions like `len()`, `min()`, `max()`, and `sum()` used to perform operations on sequences.

  - **List, Set, and Dictionary Comprehensions**:
    - Compact way to process sequences and create new lists, sets, or dictionaries.
    - Syntax: `[expression for item in iterable if condition]`.
- **Functions**: Outlines function definition, scope, lambda functions, and advanced function constructs like decorators and generators.
  - **Namespaces, Scope, and Local Functions**:
    - Understanding how Python manages names and their scopes.
    - Local functions are functions defined within other functions.

  - **Returning Multiple Values**:
    - Functions can return multiple values using tuples.

  - **Functions Are Objects**:
    - Functions can be assigned to variables, passed as arguments, and returned from other functions.

  - **Anonymous (Lambda) Functions**:
    - Small, unnamed functions defined using the `lambda` keyword.
    - Syntax: `lambda arguments: expression`.

  - **Generators**:
    - Functions that yield items one at a time, using `yield` keyword.
    - Used for creating iterators.

  - **Errors and Exception Handling**:
    - Handling exceptions using `try`, `except`, `else`, and `finally` blocks.
- **Files and the Operating System**: Explains file handling, reading and writing data, and interfacing with the operating system for file operations.
  - **Reading and Writing Files**:
    - Using `open()`, `read()`, and `write()` functions to handle files.
    - Context manager `with` statement to ensure proper file closing.

  - **Bytes and Unicode with Files**:
    - Handling different encodings and binary data.
    - Ensuring correct file encoding with the `encoding` parameter in `open()`.

## NumPy Basics: Arrays and Vectorized Computation
- **NumPy ndarray**: Explores the array object and its grid of elements of the same type, detailing array creation, data types, and array operations.
  - **Creating ndarrays**:
    - Arrays can be created using functions like `np.array()`, `np.zeros()`, `np.ones()`, `np.empty()`, and `np.arange()`.
    - The `dtype` attribute defines the data type of the elements in the array.

  - **Data Types for ndarrays**:
    - NumPy supports a variety of data types including integers, floats, and more specialized types like `complex`.

  - **Arithmetic with NumPy Arrays**:
    - NumPy allows element-wise operations, meaning operations are performed on each element of the array independently.
    - Supports operations like addition, subtraction, multiplication, and division between arrays and scalars.

  - **Basic Indexing and Slicing**:
    - Arrays can be indexed and sliced using square brackets. 
    - Supports slicing similar to Python lists, but also allows slicing in multiple dimensions.

  - **Boolean Indexing**:
    - Arrays can be filtered using boolean arrays.
    - Example: `data[data > 0]` selects all positive elements from `data`.

  - **Fancy Indexing**:
    - Allows the use of integer arrays to index into another array.
    - Useful for reordering and filtering data.

  - **Transposing Arrays and Swapping Axes**:
    - Transposing with `.T` flips rows and columns.
    - `np.transpose()` and `.swapaxes()` allow for more complex reordering of dimensions.
- **Pseudorandom Number Generation**: Discusses universal functions (ufuncs) for performing element-wise operations and data processing.
  - **np.random**: Provides functions for generating random numbers.
  - Includes functions for random sampling, generating random numbers from different distributions, and more.
- **Functions for Fast Array Processing**: Discusses universal functions (ufuncs) for performing element-wise operations and data processing.
  - **Universal Functions (ufuncs)**:
    - Perform element-wise operations on arrays.
    - Examples include `np.sqrt()`, `np.exp()`, and trigonometric functions like `np.sin()`.
- **Array-Oriented Programming with Arrays**:
  - **Expressing Conditional Logic as Array Operations**:
    - Conditional operations can be performed using `np.where()`.
    - Example: `np.where(condition, x, y)` returns elements from `x` where `condition` is True, and from `y` where it is False.

  - **Mathematical and Statistical Methods**:
    - Methods like `np.mean()`, `np.sum()`, `np.std()`, and `np.var()` perform statistical operations on arrays.
    - Axis-specific operations are supported.

  - **Methods for Boolean Arrays**:
    - Boolean arrays can be used to count or sum up the number of True values using methods like `np.sum()` on boolean arrays.

  - **Sorting**:
    - Arrays can be sorted using `np.sort()`.
    - `np.argsort()` returns the indices that would sort an array.

  - **Unique and Other Set Logic**:
    - Functions like `np.unique()`, `np.in1d()`, `np.intersect1d()`, and `np.setdiff1d()` perform set operations on arrays.
- **File Input and Output with Arrays**
  - **np.save() and np.load()**: Functions for saving and loading arrays to and from disk.
  - **np.savetxt() and np.loadtxt()**: Functions for reading and writing text files.

- **Linear Algebra**
  - Includes functions for matrix multiplication (`np.dot()`), computing inverses (`np.linalg.inv()`), determinants (`np.linalg.det()`), and eigenvalues (`np.linalg.eig()`).
- **Random Walks**
  - Demonstrates how to use NumPy to simulate random processes like random walks.
  - Example code for generating and analyzing multiple random walk simulations.

## Getting Started with pandas
- **Data Structures**: Introduction to Series and DataFrame structures for handling one-dimensional and two-dimensional data respectively.
  - **Series**:
    - One-dimensional array-like object containing a sequence of values and an associated array of data labels (index).
    - Created using `pd.Series(data, index=index)`.

  - **DataFrame**:
    - Two-dimensional tabular data structure with labeled axes (rows and columns).
    - Created using `pd.DataFrame(data, columns=columns, index=index)`.
    - Can be thought of as a dict of Series objects.

  - **Index Objects**:
    - pandas' foundational data structure for axis labels.
    - Immutable and hold the axis labels and metadata (such as names or axis names).
- **Essential DataFrame Operations**: Focuses on data indexing, selection, filtering, dropping entries, and function application.
  - **Reindexing**:
    - Creating a new object with a new index.
    - Example: `df.reindex(new_index)`.

  - **Dropping Entries from an Axis**:
    - Removing rows or columns.
    - Example: `df.drop(labels, axis=0)` for rows or `df.drop(labels, axis=1)` for columns.

  - **Indexing, Selection, and Filtering**:
    - Selecting data using `[]`, `.loc[]`, and `.iloc[]`.
    - Boolean indexing for filtering data based on conditions.

  - **Arithmetic and Data Alignment**:
    - Arithmetic operations align on both row and column labels.
    - Operations between DataFrame and Series are similar to broadcasting.

  - **Function Application and Mapping**:
    - Applying functions element-wise, row-wise, or column-wise.
    - Example: `df.apply(np.mean, axis=0)`.

  - **Sorting and Ranking**:
    - Sorting by index or values using `df.sort_index()` and `df.sort_values()`.
    - Ranking data using `df.rank()`.

  - **Axis Indexes with Duplicate Labels**:
    - Handling duplicate labels in an index.
- **Summarizing and Computing Descriptive Statistics**
  - **Descriptive Statistics**:
    - Methods like `sum()`, `mean()`, `std()`, `min()`, `max()`, and `describe()` to summarize data.

  - **Correlation and Covariance**:
    - Computing pairwise correlations and covariances using `df.corr()` and `df.cov()`.

  - **Unique Values, Value Counts, and Membership**:
    - Finding unique values with `pd.unique()`.
    - Counting occurrences with `pd.value_counts()`.
    - Checking membership with `pd.Series.isin()`.

## Data Loading, Storage, and File Formats
- **Reading and Writing Data**: Detailed coverage of using pandas to handle CSV, Excel, JSON, HTML, and HDF5 formats.
  - **Reading Text Files**:
    - Functions like `pd.read_csv()` for reading delimited data.
    - `pd.read_fwf()` for fixed-width formatted files.
    - Reading data from the clipboard with `pd.read_clipboard()`.
  - **Reading Text Files in Pieces**:
    - Handling large files by reading in chunks using the `chunksize` parameter.
  - **Writing Data to Text Format**:
    - Writing DataFrame to CSV with `df.to_csv()`.
  - **Working with Other Delimited Formats**:
    - Customizing delimiters, handling missing values, and specifying columns.
- **Binary Data Formats**
  - **Reading and Writing Excel Files**:
    - Using `pd.read_excel()` to read Excel files.
    - Writing to Excel with `df.to_excel()`.
  - **Using HDF5 Format**:
    - HDF5 is a binary data format that supports large datasets.
    - Functions like `pd.HDFStore()` to read/write HDF5 files.
- **Interacting with Web APIs**
  - Accessing data from web APIs using Python libraries such as `requests`.
  - Parsing JSON data returned from APIs with `pd.read_json()`.
- **Interacting with Web APIs**
    - Using SQLAlchemy to connect to databases.
    - Reading from databases with `pd.read_sql()`.
    - Writing to databases with `df.to_sql()`.

## Data Cleaning and Preparation
- **Handling Missing Data**: Discusses strategies for cleaning datasets that include null or missing data.
  - **Detecting Missing Data**:
    - Using functions like `pd.isna()` and `pd.notna()` to identify missing data.
    - The `DataFrame.isna()` method returns a DataFrame of booleans indicating missing values.

  - **Filling in Missing Data**:
    - Methods like `fillna()` to replace missing values with a specified value.
    - Using forward fill (`ffill`) and backward fill (`bfill`) methods to propagate the last valid observation or the next valid observation, respectively.

  - **Removing Missing Data**:
    - The `dropna()` method removes missing data from a DataFrame or Series.
    - Options to remove rows or columns with missing data using parameters like `axis` and `how`.
- **Data Transformations**: Covers replacing values, renaming axis indexes, and discretizing and binning continuous variables.
  - **Removing Duplicates**:
    - The `drop_duplicates()` method removes duplicate rows from a DataFrame.
    - The `duplicated()` method identifies duplicate rows.

  - **Transforming Data Using a Function or Mapping**:
    - Using functions like `map()` and `apply()` to transform data.
    - Applying functions element-wise using `applymap()` for DataFrames.

  - **Replacing Values**:
    - The `replace()` method replaces specified values with another value.
    - Useful for data cleaning tasks such as standardizing categories or correcting typos.

  - **Renaming Axis Indexes**:
    - Methods like `rename()` to rename the labels of rows or columns.
    - Using dictionaries or functions to rename axes.

  - **Discretization and Binning**:
    - Using `cut()` and `qcut()` functions to segment and sort data values into bins.
    - Creating custom bins based on specific ranges or quantiles.

  - **Detecting and Filtering Outliers**:
    - Identifying outliers using statistical methods.
    - Filtering out outliers based on conditions or thresholds.
- **String Manipulation**: Introduces string object methods and regular expressions for vectorized string operations.
  - **Vectorized String Functions**:
    - String methods available through the `.str` attribute of Series.
    - Functions like `str.contains()`, `str.replace()`, `str.findall()`, and more.

  - **Regular Expressions**:
    - Using regular expressions for advanced string pattern matching and manipulation.
    - Functions like `str.extract()` and `str.extractall()` for extracting matched patterns.
**Combining and Merging Data Sets**:
  - **Database-Style DataFrame Joins**:
    - Using `merge()` to combine DataFrames based on keys or indexes.
    - Different types of joins: inner, outer, left, and right joins.

  - **Concatenating Along an Axis**:
    - The `concat()` function for concatenating DataFrames along rows or columns.
    - Using parameters like `axis` and `ignore_index`.

  - **Combining Data with Overlap**:
    - Functions like `combine_first()` to combine overlapping DataFrames, prioritizing non-missing data.

## Data Wrangling: Join, Combine, and Reshape
- **Hierarchical Indexing**
  - **Introduction to Hierarchical Indexing**:
    - Allows multiple levels of indexing on an axis.
    - Provides a way to work with higher-dimensional data in a lower-dimensional form.

  - **Reordering and Sorting Levels**:
    - Methods like `swaplevel()`, `sort_index()` to rearrange and sort levels.

  - **Summary Statistics by Level**:
    - Using `sum()`, `mean()`, etc., with `level` parameter to aggregate data by level.
- **Combining and Merging Datasets**
  - **Database-Style DataFrame Joins**:
    - `merge()` function to perform joins similar to SQL.
    - Different types of joins: inner, outer, left, and right joins.

  - **Merging on Index**:
    - Joining DataFrames on their index using `join()` method.

  - **Concatenating Along an Axis**:
    - `concat()` function to concatenate DataFrames along rows or columns.
    - Using parameters like `axis`, `ignore_index`, and `keys`.

  - **Combining Data with Overlap**:
    - `combine_first()` method to combine overlapping DataFrames, prioritizing non-missing data.
- **Reshaping and Pivoting**
  - **Reshaping with Hierarchical Indexing**:
    - `stack()` method to pivot columns into rows.
    - `unstack()` method to pivot rows into columns.

  - **Pivoting “Long” to “Wide” Format**:
    - `pivot()` and `pivot_table()` functions to transform data from long to wide format.
- **Data Transformation**
  - **Removing Duplicates**:
    - `drop_duplicates()` to remove duplicate rows.
    - `duplicated()` to identify duplicate rows.

  - **Transforming Data Using a Function or Mapping**:
    - Applying functions element-wise with `apply()`, `map()`, and `applymap()`.

  - **Replacing Values**:
    - `replace()` method to replace specified values.

  - **Renaming Axis Indexes**:
    - `rename()` method to rename labels of rows or columns.

  - **Discretization and Binning**:
    - `cut()` and `qcut()` functions to segment and sort data values into bins.

  - **Detecting and Filtering Outliers**:
    - Identifying and filtering outliers based on conditions or thresholds.
- **String Manipulation**
  - **Vectorized String Functions**:
    - String methods available through the `.str` attribute of Series.

  - **Regular Expressions**:
    - Using regular expressions for advanced string pattern matching and manipulation.

## Plotting and Visualization
- **matplotlib Basics**: Basic plotting functions and figure customization.
  - **Figures and Subplots**:
    - The `figure()` function creates a new figure.
    - `subplots()` can be used to create multiple subplots within a single figure.
    - `add_subplot()` adds individual subplots to a figure.

  - **Colors, Markers, and Line Styles**:
    - Customizing plots with different colors, markers, and line styles.
    - Parameters like `color`, `marker`, and `linestyle`.

  - **Ticks, Labels, and Legends**:
    - Customizing ticks and labels on the x and y axes.
    - Adding legends to plots using `legend()`.

  - **Annotations and Drawing on a Subplot**:
    - Adding annotations to plots with `annotate()`.
    - Drawing shapes and text on plots using `text()`, `arrow()`, and other drawing functions.
- **Plotting with pandas**: Built-in methods for making line plots, bar plots, histograms, and scatter plots directly from pandas objects.
  - **Line Plots**:
    - Using `plot()` for simple line plots.
    - Plotting time series data.

  - **Bar Plots**:
    - Creating bar plots with `plot(kind='bar')` and `plot(kind='barh')`.

  - **Histograms and Density Plots**:
    - Using `plot(kind='hist')` for histograms.
    - Using `plot(kind='kde')` for kernel density estimates.

  - **Scatter Plots**:
    - Creating scatter plots with `plot(kind='scatter')`.
    - Customizing scatter plots with additional parameters.

- **Advanced Data Visualization**: Introduces seaborn for making statistical plots and further customization of plots using matplotlib’s settings.
  - **Categorical Data Plots**:
    - Using Seaborn for advanced categorical data plotting.
    - Functions like `catplot()`, `stripplot()`, and `swarmplot()`.

  - **Distribution Plots**:
    - Visualizing distributions with Seaborn’s `distplot()`, `kdeplot()`, and `rugplot()`.

  - **Matrix Plots**:
    - Creating heatmaps and clustermaps with `heatmap()` and `clustermap()`.

## Data Aggregation and Group Operations
- **GroupBy Mechanics**: Explains using the split-apply-combine pattern with pandas' `groupby` method for data aggregation.
  - **Splitting Data into Groups**:
    - Using the `groupby()` function to split data into groups based on some criteria.
    - The result is a `GroupBy` object, which can be iterated over like a dictionary of groups.

  - **Iterating Over Groups**:
    - Example: `for name, group in df.groupby('key')` to iterate over each group.
    - Using multiple keys for grouping by passing a list of column names to `groupby()`.

  - **Selecting a Column or Subset of Columns**:
    - Selecting a single column for aggregation: `df.groupby('key')['column']`.
    - Selecting multiple columns: `df.groupby('key')[['column1', 'column2']]`.
- **Data Aggregation**
  - **Aggregations**:
    - Common aggregation methods: `sum()`, `mean()`, `size()`, `count()`, `min()`, `max()`.
    - Using the `agg()` method to apply multiple aggregation functions at once.

  - **Group-wise Operations and Transformations**:
    - Applying functions to each group: `apply()` method.
    - Transforming data within groups: `transform()` method to apply functions and return an aligned result.
- **General split-apply-combine**: Comprehensive guide on using `apply` for general-purpose aggregation across DataFrame rows and columns.
  - **Split-Apply-Combine Pattern**:
    - Splitting data into groups, applying a function to each group, and combining the results.
    - Using the `apply()` method for custom group-wise operations.

  - **Example: Group-wise Standardization**:
    - Applying a standardization function to each group in the DataFrame.
- **Pivot Tables and Cross-Tabulation**: Techniques for creating pivot tables to summarize data and using cross-tabulation for frequency tables.
  - **Pivot Tables**:
    - Creating pivot tables with the `pivot_table()` method.
    - Parameters like `values`, `index`, `columns`, `aggfunc`, and `margins`.

  - **Cross-Tabulations**:
    - Using `pd.crosstab()` to compute a cross-tabulation of two or more factors.
    - Analyzing categorical data with cross-tabulations.
- **Example: Group-wise Linear Regression**
  - Performing linear regression on each group using the `apply()` method.
  - Combining the results of linear regression for each group.

## Time Series
- **Date and Time Data Types and Tools**: Conversion between string formats and datetime objects, handling time zones.
  - **Python Standard Library Modules**:
    - `datetime`, `time`, and `calendar` modules for handling date and time data.
  - **Converting Between String and Datetime**:
    - `pd.to_datetime()` function to parse dates from strings.
- **Time Series Basics**: Indexing, selection, and subsetting large time series data.
  - **DatetimeIndex**:
    - Creating and using `DatetimeIndex` for time series data.
  - **Indexing, Selection, Subsetting**:
    - Indexing with `DatetimeIndex`, selecting specific time periods, and subsetting data.
- **Time Series with Duplicate Indices**
  - Managing time series data with duplicate timestamps.
  - `is_unique` property to check for duplicates and `groupby()` to handle duplicates.
- **Date Ranges, Frequencies, and Shifting**: Generating date ranges and employing frequency conversion and data shifting.
  - **Generating Date Ranges**:
    - `pd.date_range()` for creating fixed-frequency date ranges.
  - **Frequencies and Offsets**:
    - Frequency strings like `'D'`, `'M'`, `'H'` for specifying date ranges.
    - Using `DateOffset` for custom date manipulations.
  - **Shifting Data**:
    - Shifting time series data forward or backward using `.shift()`.
    - Applying lagged calculations with `.shift()`.
- **Time Zone Handling**
  - Using the `pytz` library for time zone handling.
  - Localizing and converting time zones with `.tz_localize()` and `.tz_convert()`.
- **Periods and Period Arithmetic**: Usage of period data types and operations, converting between timestamps and periods.
  - Using `Period` and `PeriodIndex` for representing time spans.
  - Converting between `Timestamp` and `Period`.
- **Resampling and Frequency Conversion**: High- and low-frequency data resampling methods for time series.
  - **Resampling**:
    - Upsampling and downsampling time series data with `.resample()`.
    - Aggregation methods like `.mean()`, `.sum()`, and `.ohlc()` during resampling.
  - **Moving Window Functions**:
    - Applying rolling window calculations with `.rolling()` and `.expanding()`.
- **Time Series Plotting with pandas**
  - Built-in plotting capabilities for time series data using `.plot()`.
  - Customizing plots with Matplotlib.

## Advanced pandas
- **Categorical Data**: Introduction to categorical type in pandas for efficient storage and computation.
  - **Categorical Type**:
    - Using the `Categorical` data type for text or string data that takes on a limited, fixed number of possible values.
    - Reduces memory usage and enhances performance for certain operations.

  - **Creating Categorical Objects**:
    - Converting a column to a categorical type using `pd.Categorical` or the `.astype('category')` method.

  - **Computations with Categoricals**:
    - Operations like grouping by a categorical column can be much faster.
    - Efficient handling of categorical data in groupby operations.

  - **Methods for Categorical Data**:
    - `cat.codes` to access the integer codes for the categories.
    - `cat.categories` to access the category labels.
    - Methods like `add_categories()`, `remove_categories()`, and `rename_categories()` for modifying categories.
- **Advanced GroupBy Use**: More sophisticated examples of using `groupby` with custom aggregation functions.
  - **Group Transforms and “Unwrapped” GroupBys**:
    - Using the `transform()` method to apply a function to each group and produce an aligned result.
    - Applying multiple functions to groups with the `agg()` method.
    - Using custom aggregation functions with `agg()`.

  - **Group Weighted Average and Correlation**:
    - Calculating weighted averages within groups.
    - Group-wise correlations and applying other statistical operations within groups.
- **Techniques for Method Chaining with pipe**: Method chaining to condense and streamline data transformations.
  - Using the `pipe()` method to improve the readability of chained operations.
  - Allows for more readable and concise code when applying multiple functions sequentially.
- **Reshaping and Pivoting**
  - **Reshaping with MultiIndex**:
    - Using hierarchical indexing for reshaping data.
    - `stack()` and `unstack()` methods to pivot data from wide to long format and vice versa.

  - **Pivot Tables**:
    - Creating pivot tables with `pivot_table()`, specifying values, indexes, columns, and aggregation functions.
    - Adding margins to pivot tables to show totals.
- **Working with Time Series Data**
  - **Time Series Frequency Conversion**:
    - Converting time series data to different frequencies using `resample()`.
    - Aggregation and frequency conversion with resampling.

  - **Moving Window Functions**:
    - Applying moving window operations with `rolling()` and `expanding()`.
    - Using `ewm()` for exponentially weighted functions.
- **Performance Enhancements**:
  - Tips for optimizing performance when working with large datasets.
  - Importance of using the appropriate data types and efficient algorithms.

## Advanced NumPy

**Advanced Array Manipulation**
  - **Reshaping Arrays**:
    - Techniques for changing the shape of arrays using `reshape()`, `ravel()`, and `flatten()`.
    - Understanding array views versus copies.

  - **C- and Fortran-Contiguous**:
    - Explanation of memory layouts: C-contiguous (row-major order) and Fortran-contiguous (column-major order).
    - Impact of memory layout on performance and interoperability with other libraries.

  - **Broadcasting**:
    - Rules and techniques for broadcasting, which allows for vectorized operations on arrays of different shapes.
    - Practical examples to illustrate how broadcasting works.

**Advanced ufunc Features**
  - **Custom ufuncs**:
    - Creating custom universal functions (ufuncs) using `np.frompyfunc()` and `np.vectorize()`.
    - Enhancing performance with custom ufuncs.

  - **Reduction Operations**:
    - Using reduction operations like `reduce()`, `accumulate()`, and `reduceat()`.
    - Applying these operations for efficient array computations.

**Structured and Record Arrays**
  - **Structured Arrays**:
    - Creating structured arrays with multiple named fields.
    - Accessing and manipulating structured data.

  - **Record Arrays**:
    - Working with record arrays for more flexible data access patterns.
    - Conversion between structured arrays and record arrays.

**More About Sorting**
  - **Sorting Algorithms**:
    - Different sorting algorithms available in NumPy (`quicksort`, `mergesort`, `heapsort`, `stable`).
    - Performance considerations and use cases for each algorithm.

  - **Indirect Sorts**:
    - Techniques for indirect sorting using `argsort()` and `lexsort()`.
    - Use cases for sorting by multiple keys.

  - **Partitioning**:
    - Efficiently finding the k-th smallest elements using `partition()` and `argpartition()`.

**Writing Fast NumPy Functions**
  - **Using Cython**:
    - Introduction to Cython for writing C extensions for Python.
    - Examples of how to speed up NumPy operations using Cython.

  - **Interfacing with C Libraries**:
    - Techniques for interfacing NumPy with C libraries to leverage performance gains.
    - Practical examples of wrapping C code with NumPy arrays.

**Advanced Array Input and Output**
  - **Memory-Mapped Files**:
    - Using memory-mapped files for efficient disk-based array storage.
    - Practical applications for handling large datasets that do not fit into memory.

  - **HDF5 and Other Array Storage Options**:
    - Overview of HDF5 format for storing large numerical data.
    - Using `h5py` and `PyTables` for working with HDF5 files.