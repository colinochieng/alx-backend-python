#!/usr/bin/env python3
'''
Module for showcasing async comprehension operations
'''
from typing import Generator, List

async_generator: Generator[float, None, None] = __import__(
    '0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    description: function to exemplify async comprehension: utilizes
            yileds from async_generator
    Args: (None)
    return: a list of randomized float values from 0 to 10
    '''
    result: List[float] = [item async for item in async_generator()]

    return result
