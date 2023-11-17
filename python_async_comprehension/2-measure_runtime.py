#!/usr/bin/env python3
"""
async coroutine "measure_runtime"
"""
import asyncio
import time
from random import uniform

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures time of async comprehension
    """
    tasks = []
    first_moment = time.time()
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))

    # Run the unpacked list tasks in parallel
    results = await asyncio.gather(*tasks)
    second_moment = time.time()
    elapsed_time = second_moment - first_moment
    return elapsed_time
