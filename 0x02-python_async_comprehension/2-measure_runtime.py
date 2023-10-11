#!/usr/bin/env python3
'''
a module to measure the runtime of four parallel comprehensions
'''


from typing import List
import asyncio
import time

async_comprehension: List[float] = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    description: coroutine that will execute async_comprehension
        four times in parallel using asyncio.gather
    Args: none
    return: the total runtime and return it
    '''
    curr_t: float = time.perf_counter()
    tasks: List[asyncio.Task] = [async_comprehension() for _ in range(4)]

    await asyncio.gather(*tasks)

    return time.perf_counter() - curr_t
