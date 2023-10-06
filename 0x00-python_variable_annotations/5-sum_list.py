#!/usr/bin/env python3
'''
Module for a function to compute the sum of the elements if a list
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    :description: computes the sum
    :param input_list: a parameter of type list containing floats
    :return: sum of the elements
    """
    sum: float = 0
    for ele in input_list:
        sum += ele

    return sum
