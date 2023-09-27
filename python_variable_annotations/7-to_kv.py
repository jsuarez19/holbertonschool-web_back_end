#!/usr/bin/env python3
"""
Type-annotated function "to_kv"
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Receives a str 'k' and and an int OR float 'v'
    Returns a tuple
    """
    sqr: float = v ** 2
    output: Tuple = (k, sqr)
    return output
