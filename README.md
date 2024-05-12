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
- **Installation and Setup**: Provides detailed guidance for setting up Python and necessary libraries using Miniconda and conda-forge.
- **Navigating the Book**: Outlines how to approach the book based on readers’ familiarity with Python, detailing the structure and flow of content.
- **Community and Conferences**: Encourages engagement with the Python data science community and participation in relevant conferences.

## Python Language Basics, IPython, and Jupyter Notebooks
- **Python Interpreter**: Discusses the use of Python as an interpreted language and introduces the interactive Python interpreter.
- **IPython Basics**: Describes the advanced features of IPython, including tab completion, object introspection, and embedded shell commands.
- **Jupyter Notebooks**: Explains how to use Jupyter Notebooks for combining executable code, rich text, and graphics in a web-based interface.
- **Python Language Basics**: Covers Python syntax, built-in data structures like lists, dictionaries, sets, tuples, functions, and file operations.

## Built-In Data Structures, Functions, and Files
- **Data Structures and Sequences**: Details the use of tuples, lists, dictionaries, and sets, including comprehensive examples and special methods.
- **Functions**: Outlines function definition, scope, lambda functions, and advanced function constructs like decorators and generators.
- **Files and the Operating System**: Explains file handling, reading and writing data, and interfacing with the operating system for file operations.

## NumPy Basics: Arrays and Vectorized Computation
- **NumPy ndarray**: Explores the array object and its grid of elements of the same type, detailing array creation, data types, and array operations.
- **Functions for Fast Array Processing**: Discusses universal functions (ufuncs) for performing element-wise operations and data processing.
- **Indexing and Slicing**: Details techniques for accessing and modifying array elements.
- **Data Processing Using Arrays**: Illustrates methods such as filtering, transforming, and aggregation using array expressions.
- **File Input and Output**: Covers saving and loading array data to disk using binary formats or integrating with pandas.

## Getting Started with pandas
- **Data Structures**: Introduction to Series and DataFrame structures for handling one-dimensional and two-dimensional data respectively.
- **Essential DataFrame Operations**: Focuses on data indexing, selection, filtering, dropping entries, and function application.
- **Handling Missing Data**: Techniques for identifying, filtering, and filling missing data.
- **Hierarchical Indexing**: Explains multiple (two or more) index levels on an axis.

## Data Loading, Storage, and File Formats
- **Reading and Writing Data**: Detailed coverage of using pandas to handle CSV, Excel, JSON, HTML, and HDF5 formats.
- **Data Cleaning Techniques**: Includes removing duplicates, replacing values, and manipulating strings.
- **Data Transformation**: Conversion operations and text data manipulation are explained.

## Data Cleaning and Preparation
- **Handling Missing Data**: Discusses strategies for cleaning datasets that include null or missing data.
- **Data Transformations**: Covers replacing values, renaming axis indexes, and discretizing and binning continuous variables.
- **String Manipulation**: Introduces string object methods and regular expressions for vectorized string operations.

## Data Wrangling: Join, Combine, and Reshape
- **Merging Datasets**: Uses pandas merge function to combine datasets based on one or more keys.
- **Concatenating Along an Axis**: Concatenation and "binding" operations with utilities from pandas.
- **Combining Data with Overlap**: Discusses combining overlapping data sets using `where` methods.
- **Pivoting “Long” to “Wide” Format**: Techniques for transforming datasets between long and wide formats.

## Plotting and Visualization
- **matplotlib Basics**: Basic plotting functions and figure customization.
- **Plotting with pandas**: Built-in methods for making line plots, bar plots, histograms, and scatter plots directly from pandas objects.
- **Advanced Data Visualization**: Introduces seaborn for making statistical plots and further customization of plots using matplotlib’s settings.

## Data Aggregation and Group Operations
- **GroupBy Mechanics**: Explains using the split-apply-combine pattern with pandas' `groupby` method for data aggregation.
- **Column-Wise and Multiple Function Application**: Details applying multiple aggregation functions to DataFrame columns using `agg` and `transform`.
- **General split-apply-combine**: Comprehensive guide on using `apply` for general-purpose aggregation across DataFrame rows and columns.
- **Pivot Tables and Cross-Tabulation**: Techniques for creating pivot tables to summarize data and using cross-tabulation for frequency tables.

## Time Series
- **Date and Time Data Types and Tools**: Conversion between string formats and datetime objects, handling time zones.
- **Time Series Basics**: Indexing, selection, and subsetting large time series data.
- **Date Ranges, Frequencies, and Shifting**: Generating date ranges and employing frequency conversion and data shifting.
- **Periods and Period Arithmetic**: Usage of period data types and operations, converting between timestamps and periods.
- **Resampling and Frequency Conversion**: High- and low-frequency data resampling methods for time series.
- **Moving Window Functions**: Utilizing moving window operations for smoothing or other rolling computations.

## Advanced pandas
- **Categorical Data**: Introduction to categorical type in pandas for efficient storage and computation.
- **Advanced GroupBy Use**: More sophisticated examples of using `groupby` with custom aggregation functions.
- **Techniques for Method Chaining**: Method chaining to condense and streamline data transformations.
- **Pivot and Melt for Unstacking**: Advanced reshaping techniques involving pivot, melt, and `stack`.
- **Advanced Data Aggregation**: Explores further capabilities of `groupby` for complex data aggregation scenarios.