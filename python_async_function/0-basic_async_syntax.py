#!/usr/bin/env python3
"""
async function "wait_random"
"""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """
    Waits for a random delay between
    0 and max_delay seconds and returns it.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
