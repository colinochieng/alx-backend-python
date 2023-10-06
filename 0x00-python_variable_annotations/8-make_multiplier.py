#!/usr/bin/env python3
'''
Module for function make_multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    :description: computes a callable
    :multiplier: a float multiplier as argument
    :return: a function that multiplies a float by multiplier
    '''
    def multiplier_callable(num: float) -> float:
        '''
        :description: closed function using the multiplier for computation
        :num: parameter to multiply with multiplier
        :return: product
        '''

        return num * multiplier

    return multiplier_callable
