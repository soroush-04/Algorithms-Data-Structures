"""
Jewels and Stones
"""

from __future__ import annotations
from typing import List, Optional


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0

        j_set = set(i for i in jewels)

        for i in stones:
            if i in j_set:
                counter += 1

        return counter
