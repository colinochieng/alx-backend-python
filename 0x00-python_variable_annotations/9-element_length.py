#!/usr/bin/env python3
'''
Module for practicing Python type hint annotation
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    :descrption: computes list of sequence
    :lst: sequence
    :return: list of len of elements in the sequence
    """
    return [(i, len(i)) for i in lst]
