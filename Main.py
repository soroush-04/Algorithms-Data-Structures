"""
1985. Find the Kth Largest Integer in the Array
"""

from __future__ import annotations
from typing import List, Optional


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda x: int(x))

        return nums[-k]
