#!/usr/bin/env python3
"""
Type-annotated function "make_multiplier"
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Receives a float
    Returns a function that multiplies that that float by another one
    """
    def mult(n: float):
        n = multiplier * n
        return n

    return mult
