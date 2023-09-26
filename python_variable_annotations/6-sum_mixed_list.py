#!/usr/bin/env python3
"""
Type-annotated function "sum_mixed_list"
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Receives a list of floats and integers and returns the sum as float"""
    sum: float = 0
    for number in mxd_lst:
        sum = sum + number
    return sum
