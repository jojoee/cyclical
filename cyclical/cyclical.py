from typing import List, Tuple
import math


def encode(items: List[float], n: int) -> Tuple[List[float], List[float]]:
    """
    item must between 0 to n-1 for example
    - encoding hour number: 0-23
    - encoding month number: 0-11

    :param items: list of items e.g. [0, 1, 2, ...]
    :param n: maximum number of it e.g. 12 for mouth number, 24 for hour number
    :return:
    """
    sines = [math.sin(item * (2. * math.pi / n)) for item in items]
    coses = [math.cos(item * (2. * math.pi / n)) for item in items]

    return sines, coses
