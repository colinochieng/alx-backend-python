#!/usr/bin/env python3
'''
Module for execution of multiple coroutines
Uses wait_random from 0-basic_async_syntax.py module
'''
from typing import Callable, Optional, List
import asyncio

wait_random: Callable[[Optional[int]], float] = __import__(
        '0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    description: a function to spawn wait_random nth times
                to result into multiple coroutines
    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum range of delay, parameter to be
            used by wait_random function
    return: a list of all delays float values
    '''
    # arr: List[float] = []
    # for i in range(0, n):
    #     delay = await wait_random(max_delay)
    #     arr.append(delay)
    # arr = sorted(arr)
    # return arr

    delays: List[float] = []

    tasks: List[asyncio.Task] = [wait_random(max_delay) for _ in range(n)]

    results: List[float] = await asyncio.gather(*tasks)

    delays: List[float] = sorted(results)
    return delays
