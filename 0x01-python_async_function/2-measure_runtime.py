#!/usr/bin/env python3
'''
Module to measure runtime of an asyncio operation
Uses wait_n from 1-concurrent_coroutines.py module
'''
from typing import Callable, List
import asyncio
import time

wait_n: Callable[[int, int], List[float]] = __import__(
    '1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    description: records time taken for an async operation
    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum range of delay, parameter to be
            used by wait_random function
    returns: total_time / n (float)
    '''
    curr_t: float = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    return (time.perf_counter() - curr_t) / n
