#!/usr/bin/env python3
"""
Type-annotated function "sum_list"
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Receives a list of floats and returns the sum as float"""
    sum: float = 0
    for number in input_list:
        sum = sum + number
    return sum
