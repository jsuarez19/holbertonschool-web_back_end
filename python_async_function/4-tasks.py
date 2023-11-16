#!/usr/bin/env python3
"""
async function "task_wait_n"
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns 'task_wait_random' 'n' times with
    the specified max_delay
    Returns the list of all the delays
    """
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    # Run the unpacked list tasks in parallel
    results = await asyncio.gather(*tasks)
    return sorted(results)
