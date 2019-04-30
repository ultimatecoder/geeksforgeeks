#! /usr/bin/env python
"""
Collection of utilities
"""


def validate(value, constraint):
    """Validate given value with constraint

    Arguments:
        * value      : Value can be any data type value that have to checked
                       against the constrains.
        * constraint : Constraint is the callable which accepts single argument
                       of value and returns True or False based on given value.

    Exception:
        Raises `ValueError` if the given value is failing against provided
        constraint.

    Example:
        >>>validate(4, lambda v: v > 1)

    The function ends silently if given value is valid against given
    constraint.
    """
    if not constraint(value):
        message = f"Given {value} is not valid against provided constraint"
        raise ValueError(message)

