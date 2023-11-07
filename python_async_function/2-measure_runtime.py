#!/usr/bin/env python3
"""
async function "measure_time"
"""
import asyncio
from typing import List
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the runtime
    """
    total_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - total_time

    return (total_time / n)
