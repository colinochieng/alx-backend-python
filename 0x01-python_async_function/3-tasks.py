#!/usr/bin/env python3
'''
Exemplifies the asyncio.Task class
Uses wait_random from 0-basic_async_syntax.py module
'''
from typing import Callable, Optional, List
import asyncio

wait_random: Callable[[Optional[int]], float] = __import__(
    '0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    description: computes an instance of asyncio.Task module
    Args:
        max_delay (int): max range of the delaying time
    returns: object of asyncio.Task
    '''
    return asyncio.create_task(wait_random(max_delay))
