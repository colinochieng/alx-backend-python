#!/usr/bin/env python3
'''
The startup module: basics of async
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    description: an asynchronous coroutine that waits for a random delay
                between 0 and max_delay (Includes)
    Args:
        :max_delay: length of delay
    :return: float value randomly generated
    '''

    delay: float = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
