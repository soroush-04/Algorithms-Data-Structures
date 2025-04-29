"""
1985. Find the Kth Largest Integer in the Array
"""

from __future__ import annotations
from typing import List, Optional


class Solution:
    def reverse_words(self, s: str) -> str:
        words = s.split()

        return " ".join(words[::-1])


test = Solution()
print(test.reverse_words(" hello dear boss "))
