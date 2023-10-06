#!/usr/bin/penv python3
'''
Module for a function dealing with floats, ints and strings
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    :description: computes a tuple based on the give numbers
    :v: string
    :v: a union or a string
    return: computed tuple
    '''
    return (k, float(v) ** 2)
