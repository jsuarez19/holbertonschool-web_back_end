#!/usr/bin/env python3
"""
async function "measure_time"
"""
import asyncio
from typing import List
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the runtime
    """
    first_moment = time.time()
    asyncio.run(wait_n(n, max_delay))
    second_moment = time.time()
    total_time = second_moment - first_moment
    return total_time / n
