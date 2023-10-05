#!/usr/bin/env python3
"""
async function "measure_time"
"""
import asyncio
from typing import List
import time 
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns 'wait_random' 'n' times with
    the specified max_delay
    Returns the list of all the delays
    """
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))

    # Run the unpacked list tasks in parallel
    results = await asyncio.gather(*tasks)
    return sorted(results)
