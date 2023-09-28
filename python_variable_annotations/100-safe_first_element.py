#!/usr/bin/env python3
"""
Type-annotated function "element_length"

"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Receives a sequence
    Returns a the first element if the sequence exists
    Otherwise returns none
    """
    if lst:
        return lst[0]
    else:
        return None
