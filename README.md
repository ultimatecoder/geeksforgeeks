# GeeksForGeeks problem solutions 🤓

![GeeksForGeeksPractice](images/geeksforgeeks_practice.jpe)


## Description

Collection of solutions for [GeeksForGeeks][geeksforgeeks] problems. Solutions
are written in latest version of [Python][python] programming language.

### Directory structure

Below is a sample structure to understand the categorization of solutions.

```
── programs
│   ├── arrays
│   │   ├── maximum_in_struct_array.py
│   └── tests
│       └── test_arrays
```

* `program`: A top level directory where solutions to all the problems are
  stored. Child of this directory is a category directory or a test directory.

* `arrays`: Directory name is the Category of the problem. Child of this
  directory is solutions for a problems which are under [arrays] category.
  Because of space constraint, I am not explaining each and every category.

* `maximum_in_struct_array.py`: Name of the file is a title of the problem.
  Problems are child of category directory.

* `tests`: Test is a possible director which contains unit level of tests for
  all the problems.

* `test_arrays`: Child directory for test cases of dedicated category. It is
  prefixed with `test_*` where last part is the name of the category. Child of
  this directory is a collection of unit tests for individual problem.


## Dependencies

* [Python][python]
* [Pipenv][pipenv]
* [Garud][garud]


## Build

```pipenv shell```

This command will activate a virtual environment. Make sure [pipenv][pipenv] is
already installed.

```pipenv install```

This command will install the Python dependencies. The source code of the
program solutions is not dependent on any of these Python dependencies. The code
of unit tests and end to end tests is dependent on a few [Python][python]
libraries.


## Commands

```make unit-test```

This command will run the unit tests for all the solutions.

```make end-to-end-tests```

This command will run end to end test for all the programs.


## How to run a sultion program?

If you want to run the solution for **Arrays -> Maximum In Struct Array**
problem, you should follow below steps.

1. Activate the virtual environment using `pipenv shell`.
2. Move to `programs/arrays` directory.
3. Fire this command to run the program `python maximum_in_struct_array.py`.



[geeksforgeeks]: geeksforgeeks.org
[python]: python.org
[pipenv]: https://pipenv.readthedocs.io/en/latest/#install-pipenv-today
[arrays]: https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&page=1&sortBy=accuracy
[garud]: https://gist.github.com/ultimatecoder/801177083c722884d8e6ff76bb342c8d
