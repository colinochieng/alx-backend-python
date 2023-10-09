#!/usr/bin/env python3
'''
Module for execution of multiple coroutines (asyncio.Task)
Uses wait_random from 0-basic_async_syntax.py module
'''
from typing import Callable, List
import asyncio


task_wait_random: Callable[[int], asyncio.Task] = __import__(
    '3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    description: a function to spawn wait_random nth times
                to result into multiple coroutines
    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum range of delay, parameter to be
            used by wait_random function
    return: a list of all delays float values
    '''

    delays: List[float] = []

    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]

    results: List[float] = await asyncio.gather(*tasks)

    delays: List[float] = sorted(results)

    return delays
