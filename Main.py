"""
Sqrt(x)
"""

from __future__ import annotations
from typing import List, Optional


def sqrt(x):
    l = 0
    r = x

    while l <= r:
        m = (l + r) // 2

        if m * m == x:
            return m
        elif m * m > x:
            r = m - 1
        else:
            l = m + 1

    return r


print(sqrt(8))
