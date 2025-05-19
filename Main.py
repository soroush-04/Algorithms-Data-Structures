"""
2390. Removing Stars From a String
"""

from __future__ import annotations
from typing import List, Optional


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "*":
                stack.pop()
                continue
            stack.append(char)

        return "".join(stack)
