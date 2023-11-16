#!/usr/bin/env python3
"""
async coroutine "async_comprehension"
"""
import asyncio
from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Async comprehension
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result