#!/usr/bin/env python3
'''
A module for a function to operate on the list of
integers and floats
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    :description: computes sum
    :param mxd_lst: a mixed list of ints and floats
    :return: float for the total sum
    '''
    sum: float = 0.0

    for el in mxd_lst:
        sum += el

    return sum
