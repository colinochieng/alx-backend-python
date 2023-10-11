#!/usr/bin/env python3
'''
Module for startup of coroutines
Use the random module
'''
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    description: a function that functions as an async generator
        yielding values between 0 to 10 randomly
    Args: None
    return: None (yields values between 0 to 10 randomly)
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
