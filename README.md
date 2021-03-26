# pymleda 

![](https://github.com/UBC-MDS/pymleda/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pymleda/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pymleda) [![Deploy](https://github.com/UBC-MDS/pymleda/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/pymleda/actions/workflows/deploy.yml) [![Documentation Status](https://readthedocs.org/projects/pymleda/badge/?version=latest)](https://pymleda.readthedocs.io/en/latest/?badge=latest)

Python package that helps with preliminary eda for supervised machine learning tasks.

## Installation

```bash
$ pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple pymleda
```

## Features

The project aims to build a python package called `pymleda` with relevant functions to help with preliminary EDA for a given dataset as a Pandas dataframe. The package contains functions and classes that help perform various data preparation and wrangling tasks such as data splitting, exploration, imputation, and scaling. These functionalities were identified as commonly-performed tasks in supervised machine learning settings but may provide value in other project types as well.

The pymleda package will include the following classes/functions:
-	 `SupervisedData` is a wrapper class that splits a pandas dataframe into train and test sets and further into X and y subsets based on a list of user-provided columns.	
-	`dftype()` function will return the type of columns and variables for the input data frame. Furthermore, if there are non-numeric columns, it will return the unique values of non-numeric columns and their length.
-	`autoimpute_na()` function to identify and impute missing values for different attributes in a given pandas dataframe.
-	`dfscaling()` function to apply standard scaling to the numerical features in a pandas dataframe.

The `pymleda` package is intended to help with EDA for supervised machine learning tasks; there are other existing packages such as [`scikit-learn`](https://scikit-learn.org) and [`pandas`](https://pandas.pydata.org) that contain some similar functionality. For example, `pandas` provides users with separate functions such as `isnull()`, `isna()`, and `notna()` to detect missing values and ` fillna()`, ` interpolate()` to fill them. Our `pymleda` package intends to augment the existing functionality of these packages with some additional features. 

The `autoimpute_na` function will combine these two steps of identifying and imputing missing values in columns of a dataframe while taking into account the type of these columns (numeric or categorical). Moreover, `autoimpute_na` will detect some common non-standard missing values manually entered by users (e.g., "not available", "n/a", "na", "-"). The output of the `autoimpute_na` function will be a dataframe with imputed values.

In supervised machine learning, data splitting is often a multi-step process that involves splitting the dataset of interest into test and train portions and then further into X(features) and y(target class) subsets. Typically, the user has to create and keep track of different variables that hold each of these subsets of the data. SupervisedData is a wrapper class that builds upon the output of `train_test_split()` from `sklearn` and provides the user with quick access to appropriately-named attributes referring to each of these variables. These variables can then be used in subsequent steps of the machine learning pipeline.

## Dependencies

- python = "^3.8"
- pandas = "^1.2.3"
- sklearn = "^0.0"
- numpy = "^1.20.1"

## Usage

- Import the package
```Python
from pymleda import pymleda
```

- Check the datatypes and a summary of your input dataframe
```Python
summary, unique_df = pymleda.dftype(df)
```

- Impute NAs in your input dataframe
```Python
pymleda.autoimpute_na(df)
```
- Apply centering and scaling to the numeric features in your input dataframe
```Python
pymleda.dfscaling(df)
```

- Split the data into X train, y train, X test, and y test subsets in one convenient class call using `SupervisedData`
```Python
supervised_data = SupervisedData(df, x_cols = ['feature1', 'feature2'], y_cols = ['target'])
```

## Documentation

The official documentation is hosted on Read the Docs: https://pymleda.readthedocs.io/en/latest/

## Contributors

### Development Leads

- Saule Atymtayeva
- Sang Yoon Lee
- Yazan Saleh
- Tanmay Sharma

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/pymleda/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
