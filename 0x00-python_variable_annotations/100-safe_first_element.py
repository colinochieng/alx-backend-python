#!/usr/bin/env python3

'''
Module for practicing Python type hint annotation
'''
from typing import Sequence, Any, Union

# The types of the elements of the input are not know


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    :description: function to avail the first element from a sequence
    :lst: any form of sequence
    :return: any data set or None
    """
    if lst:
        return lst[0]
    else:
        return None
